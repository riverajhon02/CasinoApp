from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin , UserResponse
from app.schemas.token import Token,VerifyOTPRequest
from app.services.auth_service import create_user,generate_tokens
from app.models.refresh_token import RefreshToken
from app.core.config import settings
from app.utils.otp import generate_otp, save_otp, verify_otp
from jose import jwt
from app.core.security import create_access_token,create_temp_token,verify_temp_token
from app.schemas.refresh_token import LogoutRequest, RefreshRequest
from app.services.otp import generate_otp, save_otp
from app.services.auth_service import authenticate_user
from app.services.email_service import send_otp_email
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email, user.password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = authenticate_user(db, user.username, user.password)

    if not db_user:
        raise HTTPException(400, "Credenciales incorrectas")

    otp = generate_otp()
    save_otp(db_user.email, otp)

    send_otp_email(db_user.email, otp)

    temp_token = create_temp_token(db_user.email)

    return {
        "otp_required": True,
        "temp_token": temp_token
    }

@router.post("/verify-otp", response_model=Token)

def verify_otp_endpoint(data: VerifyOTPRequest, db: Session = Depends(get_db)):

    payload = verify_temp_token(data.temp_token)

    if not payload:
        raise HTTPException(401, "Token inválido")

    email = payload["sub"]

    if not verify_otp(email, data.otp):
        raise HTTPException(400, "OTP inválido")

    user = db.query(User).filter(User.email == email).first()

    return generate_tokens(db,user)

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