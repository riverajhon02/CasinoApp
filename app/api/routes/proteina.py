from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.proteina import ProteinaCreate, ProteinaUpdate, ProteinaOut
from app.api.controllers import proteina

router = APIRouter(prefix="/proteinas", tags=["Proteinas"])

@router.get("/", response_model=list[ProteinaOut])
def listar(db: Session = Depends(get_db)):
    return proteina.listar(db)

@router.post("/", response_model=ProteinaOut)
def crear(data: ProteinaCreate, db: Session = Depends(get_db)):
    return proteina.crear(db, data)

@router.put("/{id}", response_model=ProteinaOut)
def actualizar(id: int, data: ProteinaUpdate, db: Session = Depends(get_db)):
    result = proteina.actualizar(db, id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Proteina no encontrada")
    return result

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    result = proteina.eliminar(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Proteina no encontrada")
    return {"ok": True}