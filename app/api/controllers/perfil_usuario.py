from sqlalchemy.orm import Session
from app.schemas.perfil_usuario import PerfilUsuarioCreate,PerfilUsuarioUpdate
from app.models.perfil_usuario import PerfilUsuario
from app.crud import perfil_usuario as crud
from fastapi import HTTPException, status


def create_perfil(db: Session, perfil: PerfilUsuarioCreate, user_id: int):
    # 🔒 Validación 1: evitar duplicados
    perfil_existente = crud.get_perfil_by_user(db, user_id)
    if perfil_existente:
        # Importante: Usa HTTPException para que no de error 500
        raise HTTPException(status_code=400, detail="El usuario ya tiene un perfil")

    # 🔥 LLAMADA CORREGIDA: Pasamos los 3 argumentos que el CRUD espera
    return crud.create_perfil(db, perfil, user_id)


def get_perfil_by_user(db: Session, user_id: int):
    return db.query(PerfilUsuario).filter(
        PerfilUsuario.user_id == user_id
    ).first()

def actualizar_perfil_usuario(db: Session, perfil_id: int, data):

    db_perfil = crud.get_by_id(db, perfil_id)

    if not db_perfil:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil no encontrado"
        )

    update_data = data.dict(exclude_unset=True)

    # 🔥 Validación de correo único (si viene en el request)
    if "correo" in update_data:
        existente = crud.get_by_correo(db, update_data["correo"])

        if existente and existente.id != perfil_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe otro perfil con ese correo"
            )

    return crud.update(db, db_perfil, update_data)


def get_perfiles(db: Session):
    return crud.get_perfiles(db)


def get_perfil(db: Session, perfil_id: int):
    return crud.get_perfil_by_id(db, perfil_id)




def delete_perfil(db: Session, perfil_id: int):
    perfil = crud.get_perfil_by_id(db, perfil_id)

    if not perfil:
        return None

    crud.delete_perfil(db, perfil)
    return perfil