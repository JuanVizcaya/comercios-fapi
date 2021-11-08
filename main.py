from typing import List

from sqlalchemy.orm import Session

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, status

from database import get_db
from dependencies import get_current_comercio
from models import Comercio as ComercioModel
from models import Empleado as EmpleadoModel
from schema import ComercioCreate, ComercioRetrieve
from schema import EmpleadoCreate, EmpleadoRetrieve, EmpleadoUpdate


app = FastAPI()

@app.post("/comercios/", response_model=ComercioRetrieve)
async def add_comercio(
    comercio: ComercioCreate,
    db: Session = Depends(get_db)
    ) -> ComercioRetrieve:
    """ API: Agrega un comercio a la base de datos """

    new_comercio = ComercioModel(**comercio.dict())
    db.add(new_comercio)
    db.commit()
    return new_comercio

@app.get('/comercios/', response_model=List[ComercioRetrieve])
async def get_comercios(
    comercio: ComercioModel = Depends(get_current_comercio),
    db: Session = Depends(get_db)
    ) -> List[ComercioRetrieve]:
    """ API: Obtiene todos los comercios """

    all_comercios = db.query(ComercioModel).all()
    return all_comercios

@app.post('/empleados/', response_model=EmpleadoRetrieve)
async def add_empleado(
    empleado: EmpleadoCreate,
    comercio: ComercioModel = Depends(get_current_comercio),
    db: Session = Depends(get_db)
    ) -> EmpleadoRetrieve:
    """ API: Agrega un empleado a un comercio """

    new_empleado = EmpleadoModel(comercio=comercio.id, **empleado.dict())
    db.add(new_empleado)
    db.commit()
    return new_empleado

@app.get('/empleados/', response_model=List[EmpleadoRetrieve])
async def get_empleados(
    comercio: ComercioModel = Depends(get_current_comercio),
    db: Session = Depends(get_db)
    ) -> List[EmpleadoRetrieve]:
    """ API: Obtiene todos los empleados de un comercio """

    all_empleados = db.query(EmpleadoModel).filter(
        EmpleadoModel.comercio == comercio.id
    ).all()
    return all_empleados

@app.put('/empleados/{uuid}/', response_model=EmpleadoRetrieve)
async def update_empleado(
    uuid: str,
    empleado: EmpleadoUpdate,
    comercio: ComercioModel = Depends(get_current_comercio),
    db: Session = Depends(get_db)
    ) -> EmpleadoRetrieve:
    """ API: Actualiza un empleado del comercio"""

    empleado_to_update = db.query(EmpleadoModel).filter(
        EmpleadoModel.comercio == comercio.id,
        EmpleadoModel.uuid == uuid
    ).first()
    if not empleado_to_update:
        return status.HTTP_404_NOT_FOUND
    empleado_to_update.nombre = empleado.nombre
    empleado_to_update.apellido = empleado.apellido
    empleado_to_update.dni = empleado.dni
    empleado_to_update.telefono = empleado.telefono
    db.commit()
    return empleado_to_update

@app.delete('/empleados/{uuid}/')
async def delete_empleado(
    uuid: str,
    comercio: ComercioModel = Depends(get_current_comercio),
    db: Session = Depends(get_db)
    ) -> None:
    """ API: Elimina un empleado del comercio """

    empleado_to_delete = db.query(EmpleadoModel).filter(
        EmpleadoModel.comercio == comercio.id,
        EmpleadoModel.uuid == uuid
    ).first()
    if not empleado_to_delete:
        return status.HTTP_404_NOT_FOUND
    db.delete(empleado_to_delete)
    db.commit()
