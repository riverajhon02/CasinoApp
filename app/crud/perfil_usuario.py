
from sqlalchemy.orm import Session
from app.models.perfil_usuario import PerfilUsuario
from app.schemas.perfil_usuario import PerfilUsuarioCreate
from fastapi import HTTPException, status


def create_perfil(db: Session, perfil: PerfilUsuarioCreate, user_id: int):
    # 1. Validar si ya existe el perfil
    existing = db.query(PerfilUsuario).filter(
        PerfilUsuario.user_id == user_id
    ).first()

    if existing:
        # Usamos HTTPException para que FastAPI devuelva un error 400 en lugar de 500
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya tiene un perfil asociado"
        )

    # 2. Crear la instancia del modelo
    # Nota: Si usas Pydantic V2, es mejor usar .model_dump() en lugar de .dict()
    db_perfil = PerfilUsuario(
        **perfil.model_dump(), 
        user_id=user_id
    )

    try:
        db.add(db_perfil)
        db.commit()
        db.refresh(db_perfil)
        return db_perfil
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al guardar en la base de datos: {str(e)}"
        )

def get_perfil_by_user(db: Session, user_id: int):
    return db.query(PerfilUsuario).filter(
        PerfilUsuario.user_id == user_id
    ).first()

def delete_perfil(db: Session, perfil: PerfilUsuario):
    db.delete(perfil)
    db.commit()
    return True

def get_by_id(db: Session, perfil_id: int):
    return db.query(PerfilUsuario).filter(PerfilUsuario.id == perfil_id).first()


def get_by_correo(db: Session, correo: str):
    return db.query(PerfilUsuario).filter(PerfilUsuario.correo == correo).first()


def update(db: Session, db_perfil: PerfilUsuario, data: dict):

    for key, value in data.items():
        setattr(db_perfil, key, value)

    db.commit()
    db.refresh(db_perfil)

    return db_perfil