from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.centro_costo import CentroCosto
from app.schemas.centro_costo import CentroCostoCreate, CentroCostoUpdate
from app.crud import centro_costo


def listar_centros(db: Session, solo_activos: bool = True):
    return centro_costo.get_all(db, solo_activos)


def obtener_centro(db: Session, centro_id: int):
    centro = centro_costo.get_by_id(db, centro_id)

    if not centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de costo no encontrado"
        )

    return centro


def crear_centro(db: Session, centro: CentroCostoCreate):

    # 🔥 Validar duplicado
    existente = db.query(CentroCosto)\
        .filter(CentroCosto.nombre == centro.nombre)\
        .first()

    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un centro de costo con ese nombre"
        )

    return centro_costo.create(db, centro)


def actualizar_centro(db: Session, centro_id: int, centro: CentroCostoUpdate):

    db_centro = centro_costo.get_by_id(db, centro_id)

    if not db_centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de costo no encontrado"
        )

    # 🔥 Validar duplicado
    if centro.nombre:
        existente = db.query(CentroCosto)\
            .filter(
                CentroCosto.nombre == centro.nombre,
                CentroCosto.id != centro_id
            ).first()

        if existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe otro centro de costo con ese nombre"
            )

    return centro_costo.update(db, centro_id, centro)


def eliminar_centro(db: Session, centro_id: int):

    db_centro = centro_costo.get_by_id(db, centro_id)

    if not db_centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de costo no encontrado"
        )

    if db_centro.estado is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El centro de costo ya está inactivo"
        )

    # 🔥 AQUÍ EL FIX
    centro_costo.delete(db, db_centro)

    return {"message": "Centro de costo desactivado correctamente"}

def activar_centro(db: Session, centro_id: int):

    db_centro = centro_costo.get_by_id(db, centro_id)

    if not db_centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de costo no encontrado"
        )

    if db_centro.estado is True:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El centro de costo ya está activo"
        )

    centro_costo.activar(db, db_centro)

    return {"message": "Centro de costo activado correctamente"}