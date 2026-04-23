from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin , UserResponse
from app.schemas.token import Token
from app.services.auth_service import create_user, login_user
from app.models.refresh_token import RefreshToken
from app.core.config import settings
from jose import jwt
from app.core.security import create_access_token
from app.schemas.refresh_token import LogoutRequest, RefreshRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email, user.password)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    tokens = login_user(db, user.username, user.password)

    if not tokens:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    return tokens

@router.post("/logout")
def logout(data: LogoutRequest, db: Session = Depends(get_db)):

    db.query(RefreshToken).filter(
        RefreshToken.token == data.refresh_token
    ).delete()

    db.commit()

    return {"message": "Logout exitoso"}

@router.post("/refresh")
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):

    db_token = db.query(RefreshToken).filter(
        RefreshToken.token == data.refresh_token
    ).first()

    if not db_token:
        raise HTTPException(status_code=401, detail="Token inválido")

    payload = jwt.decode(
        data.refresh_token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

    new_access_token = create_access_token({"sub": payload["sub"]})

    return {"access_token": new_access_token}