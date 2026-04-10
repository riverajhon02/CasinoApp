from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nombre: str
    nit:str
    estado: bool = True

class EmpresaMe(BaseModel):
    nombre: str  
     
    class Config:
        from_attributes = True 

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(BaseModel):
    nombre: str | None = None
    nit: str | None = None
    estado: bool | None = None

class EmpresaResponse(EmpresaBase):
    id: int

    class Config:
        from_attributes = True