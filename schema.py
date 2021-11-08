from pydantic import BaseModel
from typing import Optional


class ComercioCreate(BaseModel):
    nombre: str
    activo: Optional[bool]
    email_contacto: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "nombre": "La Tiendita",
                "activo": True,
                "email_contacto": "latiendita@example.com"
            }
        }


class ComercioRetrieve(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    nombre: str
    activo: Optional[bool]
    email_contacto: Optional[str]
    api_key: Optional[str]

    class Config:
        orm_mode = True


class EmpleadoCreate(BaseModel):
    nombre: str
    apellidos: str
    pin: str
    activo: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "nombre": "Peter",
                "apellido": "Parker",
                "email_contacto": "pparker@avengers.com",
                "pin": "000001",
                "activo": True
            }
        }


class EmpleadoRetrieve(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    nombre: str
    apellidos: str
    pin: str
    comercio: int
    activo: Optional[bool]

    class Config:
        orm_mode = True


class EmpleadoUpdate(BaseModel):
    nombre: Optional[str]
    apellidos: Optional[str]
    pin: Optional[str]
    activo: Optional[bool]

    class Config:
        orm_mode = True
