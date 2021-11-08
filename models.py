import uuid as _uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from sqlalchemy.sql import func

from database import Base

def generate_uuid():
    return str(_uuid.uuid4())


class Comercio(Base):
    __tablename__ = 'comercio'
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    uuid = Column(String(36), default=generate_uuid, unique=True)
    nombre = Column(String(100))
    activo = Column(Boolean, default=True)
    email_contacto = Column(String(50), nullable=True)
    telefono_contacto = Column(String(15), nullable=True)
    api_key = Column(String(36), default=generate_uuid, unique=True)
    fecha_creacion = Column(DateTime, default=func.now())

    @validates('uuid')
    def validates_uuid(self, key, value):
        if self.uuid and self.uuid != value:  # Field already exists
            raise ValueError('uuid cannot be modified.')
        return value

    @validates('api_key')
    def validates_api_key(self, key, value):
        if self.api_key and self.api_key != value:  # Field already exists
            raise ValueError('api_key cannot be modified.')
        return value


class Empleado(Base):
    __tablename__ = 'empleado'
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    uuid = Column(String(36), default=generate_uuid, unique=True)
    nombre = Column(String(40))
    apellidos = Column(String(40))
    pin = Column(String(6))
    comercio = Column(BigInteger, ForeignKey('comercio.id'))
    fecha_creacion = Column(DateTime, default=func.now())
    activo = Column(Boolean, default=True)

    class Meta:
        unique_together = (('pin', 'comercio'),)

    @validates('uuid')
    def validates_uuid(self, key, value):
        if self.uuid and self.uuid != value:  # Field already exists
            raise ValueError('uuid cannot be modified.')
        return value
