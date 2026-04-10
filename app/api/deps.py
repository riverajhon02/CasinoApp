from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from fastapi import status

from app.core.config import settings
from app.db.database import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except:
        raise HTTPException(status_code=401, detail="Token inválido")

    # 🔥 AQUÍ ESTÁ LA DIFERENCIA
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user  # ✅ ahora sí es objeto

def require_role(role_name: str):
    def role_checker(user: User = Depends(get_current_user)):

        if not user.role or user.role.nombre != role_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para esta acción"
            )

        return user

    return role_checker