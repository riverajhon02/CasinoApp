from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.centro_costo import (
    CentroCostoCreate,
    CentroCostoUpdate,
    CentroCostoResponse
)
from app.db.database import get_db
from app.api.controllers import centro_costo as controller

router = APIRouter(prefix="/costos", tags=["Centros de Costo"])


@router.get("/", response_model=list[CentroCostoResponse])
def listar(
    solo_activos: bool = Query(True),
    db: Session = Depends(get_db)
):
    return controller.listar_centros(db, solo_activos)


@router.get("/{centro_id}", response_model=CentroCostoResponse)
def obtener(centro_id: int, db: Session = Depends(get_db)):
    return controller.obtener_centro(db, centro_id)


@router.post("/", response_model=CentroCostoResponse)
def crear(centro: CentroCostoCreate, db: Session = Depends(get_db)):
    return controller.crear_centro(db, centro)


@router.put("/{centro_id}", response_model=CentroCostoResponse)
def actualizar(centro_id: int, centro: CentroCostoUpdate, db: Session = Depends(get_db)):
    return controller.actualizar_centro(db, centro_id, centro)


@router.delete("/{centro_id}")
def eliminar(centro_id: int, db: Session = Depends(get_db)):
    return controller.eliminar_centro(db, centro_id)

@router.patch("/{centro_id}/activar")
def activar(
    centro_id: int,
    db: Session = Depends(get_db)
):
    return controller.activar_centro(db, centro_id)