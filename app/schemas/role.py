from pydantic import BaseModel


class RoleResponse(BaseModel):
    nombre: str

    class Config:
        from_attributes = True