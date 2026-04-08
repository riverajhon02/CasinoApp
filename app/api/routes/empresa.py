from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.empresa import EmpresaCreate, EmpresaResponse, EmpresaUpdate
from app.api.controllers import empresa as controller

router = APIRouter(prefix="/empresas", tags=["Empresas"])


@router.post("/", response_model=EmpresaResponse)
def crear(data: EmpresaCreate, db: Session = Depends(get_db)):
    return controller.crear_empresa(db, data)


@router.get("/", response_model=list[EmpresaResponse])
def listar(solo_activos: bool = True, db: Session = Depends(get_db)):
    return controller.listar_empresas(db, solo_activos)


@router.get("/{empresa_id}", response_model=EmpresaResponse)
def obtener(empresa_id: int, db: Session = Depends(get_db)):
    return controller.obtener_empresa(db, empresa_id)


@router.put("/{empresa_id}", response_model=EmpresaResponse)
def actualizar(empresa_id: int, data: EmpresaUpdate, db: Session = Depends(get_db)):
    return controller.actualizar_empresa(db, empresa_id, data)


@router.delete("/{empresa_id}")
def eliminar(empresa_id: int, db: Session = Depends(get_db)):
    return controller.eliminar_empresa(db, empresa_id)


@router.patch("/{empresa_id}/activar")
def activar(empresa_id: int, db: Session = Depends(get_db)):
    return controller.activar_empresa(db, empresa_id)