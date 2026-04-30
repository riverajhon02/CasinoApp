from sqlalchemy.orm import Session
from app.models.proteina import Proteina
from app.schemas.proteina import ProteinaCreate, ProteinaUpdate

def get_proteinas(db: Session):
    return db.query(Proteina).all()

def get_proteina(db: Session, proteina_id: int):
    return db.query(Proteina).filter(Proteina.id == proteina_id).first()

def create_proteina(db: Session, data: ProteinaCreate):
    db_obj = Proteina(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_proteina(db: Session, proteina_id: int, data: ProteinaUpdate):
    proteina = get_proteina(db, proteina_id)
    if not proteina:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(proteina, key, value)

    db.commit()
    db.refresh(proteina)
    return proteina

def delete_proteina(db: Session, proteina_id: int):
    proteina = get_proteina(db, proteina_id)
    if not proteina:
        return None

    db.delete(proteina)
    db.commit()
    return proteina