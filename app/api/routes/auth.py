from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin , UserResponse
from app.schemas.token import Token
from app.services.auth_service import create_user, login_user

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