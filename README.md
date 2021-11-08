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

**virtualenv/conda**

- `tox`

**Contenedor**

- `docker-compose run --rm api tox`

## Documentación
Documentación integrada con [openapi](https://swagger.io/specification/)

Url: 
`http://localhost:8000/docs`