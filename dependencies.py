from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from database import get_db
from models import Comercio as ComercioModel


security = HTTPBasic()

async def get_current_comercio(
    db: Session = Depends(get_db),
    credentials: HTTPBasicCredentials = Depends(security)
) -> ComercioModel:
    """ Obtiene el comercio medienta el api_key """

    print(credentials.username)
    comercio_query = db.query(ComercioModel).filter_by(
        api_key=credentials.username
    )
    if not comercio_query.count():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    comercio = comercio_query.first()
    return comercio
