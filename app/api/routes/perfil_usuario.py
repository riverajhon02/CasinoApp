from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.api.controllers.perfil_usuario import actualizar_perfil_usuario
from app.schemas.perfil_usuario import (
    PerfilUsuarioCreate,
    PerfilUsuarioResponse,
    PerfilUsuarioUpdate

)
from app.db.database import get_db
from app.api.controllers import perfil_usuario as controller

router = APIRouter(prefix="/perfil", tags=["Perfil Usuario"])

@router.post("/me", response_model=PerfilUsuarioResponse)
def create_my_profile(
    perfil: PerfilUsuarioCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return controller.create_perfil(db, perfil, current_user.id)

@router.put("/{perfil_id}", response_model=PerfilUsuarioResponse)
def update_perfil(
    perfil_id: int,
    data: PerfilUsuarioUpdate,
    db: Session = Depends(get_db)
):
    return actualizar_perfil_usuario(db, perfil_id, data)