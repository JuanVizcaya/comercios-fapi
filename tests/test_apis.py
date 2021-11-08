from requests.auth import HTTPBasicAuth

from fastapi import status
from fastapi.testclient import TestClient

from models import Empleado
from tests.database import app, TestingSessionLocal


client = TestClient(app)


def set_and_test_comercio():
    """ Test creación y respuesta de comercios """

    comercio_test_name = "Test Comercio"
    response = client.post(
        "/comercios/",
        json={"nombre": comercio_test_name}
    )
    # Respuesta debe ser 201
    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    # Nombre debe ser igual al enviado
    assert data["nombre"] == comercio_test_name
    # Comercio debe tener un id generado por la db
    assert "id" in data

    return {'api_key': data["api_key"], 'id': data["id"]}


def test_empleados():
    """ Test CRUD de empleados en comercio """

    # Crear comercio
    comercio = set_and_test_comercio()
    auth = HTTPBasicAuth(username=comercio['api_key'], password="")

    empleado_test_1 = {
        "nombre": "Empleado",
        "apellidos": "Test uno",
        "pin": "000000",
    }
    empleado_test_2 = {
        "nombre": "Empleado",
        "apellidos": "Test dos",
        "pin": "000001",
    }

    # Crear empleado
    response = client.post(
        "/empleados/",
        json=empleado_test_1,
        auth=auth
    )

    # Respuesta debe ser 201
    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()

    # Atributos deben ser igual a los enviados
    assert data["nombre"] == empleado_test_1["nombre"]
    assert data["apellidos"] == empleado_test_1["apellidos"]
    assert data["pin"] == empleado_test_1["pin"]
    assert data["activo"]
    empleado_1_uuid = data["uuid"]

    # Crear empleado 2
    response = client.post(
        "/empleados/",
        json=empleado_test_2,
        auth=auth
    )
    data = response.json()
    empleado_2_uuid = data["uuid"]

    # Obtener empleados del comercio
    response = client.get(
        "/empleados/",
        auth=auth
    )
    # Respuesta debe ser 200
    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    response_uuids = [empleado["uuid"] for empleado in data]
    # Deben estar los 2 empleados
    assert empleado_1_uuid in response_uuids
    assert empleado_2_uuid in response_uuids

    # Actualizar empleado 1
    new_data = {
        "nombre": "Empleado edited",
        "apellidos": "Test uno",
        "pin": "999999",
        "activo": False
    }
    response = client.put(
        f"/empleados/{empleado_1_uuid}/",
        json=new_data,
        auth=auth
    )
    # Respuesta debe ser 200
    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    # Atributos deben ser igual a los enviados
    assert data["nombre"] == new_data["nombre"]
    assert data["apellidos"] == new_data["apellidos"]
    assert data["pin"] == new_data["pin"]
    assert not data["activo"]

    # Eliminar empleado 1
    response = client.delete(
        f"/empleados/{empleado_1_uuid}/",
        auth=auth
    )
    # Respuesta debe ser 204
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text

    # Verificar que solo existe el empleado 2
    db = TestingSessionLocal()
    all_empleados = db.query(Empleado).filter_by(
        comercio=comercio['id']
    ).all()
    # Debe haber 1 empleado
    assert len(all_empleados) == 1
    # Debe ser el empleado 2
    assert all_empleados[0].uuid == empleado_2_uuid
