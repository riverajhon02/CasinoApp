from sqlalchemy.orm import Session
from app.models.centro_costo import CentroCosto
from app.schemas.centro_costo import CentroCostoCreate, CentroCostoUpdate


# 🔍 LISTAR
def get_all(db: Session, solo_activos: bool = True):
    query = db.query(CentroCosto)

    if solo_activos:
        query = query.filter(CentroCosto.estado == True)

    return query.all()


# 🔎 OBTENER POR ID
def get_by_id(db: Session, centro_id: int):
    return db.query(CentroCosto).filter(CentroCosto.id == centro_id).first()


# 🔍 BUSCAR POR NOMBRE (clave para validaciones)
def get_by_nombre(db: Session, nombre: str):
    return db.query(CentroCosto).filter(CentroCosto.nombre == nombre).first()


# ➕ CREAR
def create(db: Session, centro: CentroCostoCreate):
    db_centro = CentroCosto(**centro.dict())
    db.add(db_centro)
    db.commit()
    db.refresh(db_centro)
    return db_centro


# ✏️ ACTUALIZAR
def update(db: Session, db_obj: CentroCosto, centro: CentroCostoUpdate):

    update_data = centro.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


# ❌ SOFT DELETE (DESACTIVAR)
def delete(db: Session, db_obj: CentroCosto):
    db_obj.estado = False
    db.commit()
    db.refresh(db_obj)
    return db_obj

def activar(db: Session, db_obj):
    db_obj.estado = True
    db.commit()
    db.refresh(db_obj)
    return db_obj