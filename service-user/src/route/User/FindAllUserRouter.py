"""
    @name - FindAllUserRouter
    @description - Punto de entrada servicio user operacion consultar todos los user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.user.FindAllUserService import FindAllUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_USER, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_GENERIC_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_user = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_GENERIC_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

# @Rest - Consulta todos los user
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_user.get(endpoint, response_model = response, status_code= status,tags=["User"])
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())