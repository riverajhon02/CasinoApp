from pydantic import BaseModel

class ProteinaBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class ProteinaCreate(ProteinaBase):
    pass

class ProteinaUpdate(ProteinaBase):
    pass

class ProteinaOut(ProteinaBase):
    id: int

    class Config:
        from_attributes = True