from pydantic import BaseModel, EmailStr
from app.schemas.perfil_usuario import PerfilMe
from app.schemas.role import RoleResponse
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from app.schemas.perfil_usuario import PerfilUsuarioBase

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., max_length=72)

class UserLogin(BaseModel):
    username: str
    password: str

class EmpresaMe(BaseModel):
    nombre: str
    class Config:
        from_atributes = True  

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    role: Optional[RoleResponse]
    perfil: Optional[PerfilMe]
   

    class Config:
        from_attributes = True 