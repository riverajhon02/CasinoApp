from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Proteina(Base):
    __tablename__ = "proteinas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)