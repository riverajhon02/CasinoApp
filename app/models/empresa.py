from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    nit = Column(String, nullable=False, unique=True, index=True)
    estado = Column(Boolean, default=True, nullable=False)