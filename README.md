# Administración de comercios y empleados
Se trata de un FastAPI Backend, con los métodos suficientes para administrar comercios y empleados

### Requisitos

- Docker compose [Opcional](https://docs.docker.com/engine/install/)
- Conda [Opcional](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
- Python 3.9


## Instalación

- Clonar repositorio

`git clone https://github.com/JuanVizcaya/comercios-fapi.git`

**Con contenedor** (Docker)

- `cd comercios-fapi`
- `docker-compose build`

**Con virtualenv** (Python 3.9)

- `pip install venv`
- `python -m venv venv`
- `source venv/bin/activate`
- `cd comercios-fapi`
- `pip install -r requirements.txt`

**Con conda**

- `conda create -n comercios-env python=3.9`
- `conda activate comercios-env`
- `cd comercios-fapi`
- `pip install -r requirements.txt`


## Utilización

### crear .env (basado en .env.default)

- `cp .env.default .env`

### Aplicar migraciones (si es necesario)

**Contenedor**

- `docker-compose run --rm api alembic upgrade head`

**virtualenv/conda**

- `alembic upgrade head`

### Levantar el servidor

**Contenedor**

- `docker-compose up`

**virtualenv/conda**

- `uvicorn main:app --reload`


## Pruebas

Se realizaron las pruebas para el backend con [pytest](https://docs.pytest.org/en/latest/) y [flake8](https://flake8.readthedocs.io/en/latest/)

Las pruebas fueron realizadas para la creacion de comercios y el CRUD de empleados mediante su comercio asociado.

**Ejecutar con virtualenv/conda**

- `tox`

**Ejecutar con Contenedor**

- `docker-compose run --rm api tox`

## Documentación
Documentación integrada con [openapi](https://swagger.io/specification/)

Url: 
`http://localhost:8000/docs`

__nota__: Se agrega una db (sql_app.db) con información existente para hacer pruebas.