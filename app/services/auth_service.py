from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi import HTTPException, status
from app.models.user import User
from app.models.role import Role
from app.models.refresh_token import RefreshToken
from app.core.security import verify_password, hash_password, create_access_token, create_refresh_token


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None

    return user

def create_user(db: Session, username: str, email: str, password: str):

    # 🔍 1. VALIDACIONES PREVIAS (UX)
    existing_user = db.query(User).filter(User.username == username).first()
    role_user = db.query(Role).filter(Role.nombre == "USER").first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El username ya existe"
        )

    existing_email = db.query(User).filter(User.email == email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya existe"
        )

    # 🔐 2. CREAR USUARIO
    user = User(
        username=username,
        email=email,
        password=hash_password(password),
        role_id =role_user.id
    )

    # 💥 3. CONTROLAR ERRORES DE BD (concurrencia)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El usuario o email ya existe (conflicto en BD)"
        )

def login_user(db: Session, username: str, password: str):
    user = authenticate_user(db, username, password)
    
    if not user:
        return None

    access_token = create_access_token({"sub": user.username})
    refresh_token = create_refresh_token({"sub": user.username})

    # 🔥 GUARDAR EN BD
    db_token = RefreshToken(
        user_id=user.id,
        token=refresh_token,
        expires_at=datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    db.add(db_token)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }