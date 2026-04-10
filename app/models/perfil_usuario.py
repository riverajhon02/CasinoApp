from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class PerfilUsuario(Base):
    __tablename__ = "perfil_usuarios"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=True)
    centro_costo_id = Column(Integer, ForeignKey("centro_costos.id"), nullable=True)

    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    

    # Relaciones
    user = relationship("User", back_populates="perfil")
    empresa = relationship("Empresa")
    centro_costo = relationship("CentroCosto")