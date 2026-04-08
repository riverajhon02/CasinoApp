from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.empresa import Empresa
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate
from app.crud import empresa


def listar_empresas(db: Session, solo_activos: bool = True):
    return empresa.get_all(db, solo_activos)


def obtener_empresa(db: Session, empresa_id: int):
    centro = empresa.get_by_id(db, empresa_id)

    if not centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de costo no encontrado"
        )

    return centro

def crear_empresa(db: Session, data):

    if empresa.get_by_nit(db, data.nit):
        raise HTTPException(
            status_code=400,
            detail="Ya existe una empresa con ese NIT"
        )

    return empresa.create(db, data)

def actualizar_empresa(db: Session, empresa_id: int, data: EmpresaUpdate):

    db_empresa = empresa.get_by_id(db, empresa_id)

    if not db_empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa no encontrada"
        )

    
    if data.nombre:
        existente = empresa.get_by_nombre(db, data.nombre)

        if existente and existente.id != empresa_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe otra empresa con ese nombre"
            )
    return empresa.update(db, db_empresa, data)

def eliminar_empresa(db: Session, empresa_id: int):

    db_empresa = empresa.get_by_id(db, empresa_id)

    if not db_empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa no encontrada"
        )

    if db_empresa.estado is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empresa ya está inactivo"
        )

    # 🔥 AQUÍ EL FIX
    empresa.delete(db, db_empresa)

    return {"message": "Empresa eliminada correctamente"}