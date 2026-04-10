from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.empresa import EmpresaMe

class PerfilUsuarioBase(BaseModel):
    empresa_id: int
    centro_costo_id: Optional[int]
    nombres: str
    apellidos: str
    telefono: Optional[str]

class PerfilUsuarioCreate(PerfilUsuarioBase):
    pass

class EmpresaMe(BaseModel):

    nombre: str

    class Config:
        from_attributes = True

class CentroCostoMe(BaseModel):
    nombre: str

class PerfilMe(BaseModel):
    
    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    empresa: Optional[EmpresaMe] = None 
    centro_costo: Optional[CentroCostoMe] = None

    class Config:
        from_attributes = True

class PerfilUsuarioResponse(PerfilUsuarioBase):
    id: int
    user_id: int

    class Config:
        from_atributes = True

class PerfilUsuarioUpdate(BaseModel):
    empresa_id: Optional[int] = None
    centro_costo_id: Optional[int] = None

    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    telefono: Optional[str] = None

    class Config:
        from_attributes = True    