from sqlalchemy.orm import Session
from app.crud import proteina as crud

def listar(db: Session):
    return crud.get_proteinas(db)

def crear(db: Session, data):
    return crud.create_proteina(db, data)

def actualizar(db: Session, proteina_id: int, data):
    return crud.update_proteina(db, proteina_id, data)

def eliminar(db: Session, proteina_id: int):
    return crud.delete_proteina(db, proteina_id)