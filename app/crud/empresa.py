from sqlalchemy.orm import Session
from app.models.empresa import Empresa
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate


# 🔍 LISTAR
def get_all(db: Session, solo_activos: bool = True):
    query = db.query(Empresa)

    if solo_activos:
        query = query.filter(Empresa.estado == True)

    return query.all()


# 🔎 OBTENER POR ID
def get_by_id(db: Session, centro_id: int):
    return db.query(Empresa).filter(Empresa.id == centro_id).first()

def get_by_nit(db: Session, nit: str):
    return db.query(Empresa).filter(Empresa.nit == nit).first()


# 🔍 BUSCAR POR NOMBRE (clave para validaciones)
def get_by_nombre(db: Session, nombre: str):
    return db.query(Empresa).filter(Empresa.nombre == nombre).first()


# ➕ CREAR
def create(db: Session, centro: EmpresaCreate):
    db_centro = Empresa(**centro.dict())
    db.add(db_centro)
    db.commit()
    db.refresh(db_centro)
    return db_centro


# ✏️ ACTUALIZAR
def update(db: Session, db_obj: Empresa, centro: EmpresaUpdate):

    update_data = centro.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


# ❌ SOFT DELETE (DESACTIVAR)
def delete(db: Session, db_obj: Empresa):
    db_obj.estado = False
    db.commit()
    db.refresh(db_obj)
    return db_obj

def activar(db: Session, db_obj):
    db_obj.estado = True
    db.commit()
    db.refresh(db_obj)
    return db_obj