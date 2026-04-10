from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class CentroCosto(Base):
    __tablename__ = "centro_costos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True, unique=True)
    estado = Column(Boolean, default=True, nullable=False)
    perfiles = relationship("PerfilUsuario", back_populates="centro_costo")