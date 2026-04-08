from pydantic import BaseModel

class CentroCostoBase(BaseModel):
    nombre: str
    estado: bool = True

class CentroCostoCreate(CentroCostoBase):
    pass

class CentroCostoUpdate(BaseModel):
    nombre: str

class CentroCostoResponse(CentroCostoBase):
    id: int

    class Config:
        from_attributes = True