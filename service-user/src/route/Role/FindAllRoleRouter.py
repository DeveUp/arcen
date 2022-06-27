"""
    @name - FindAllRoleRouter
    @description - Punto de entrada servicio role operacion consultar todos los role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.role.FindAllRoleService import FindAllRoleService as ServiceArcen
from src.persistence.database.table.RoleTable import RoleTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_ROLE, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_GENERIC_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_ROLE+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_GENERIC_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

# @Rest - Consulta todos los role
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_role.get(endpoint, response_model = response, status_code= status,tags=["Role"])
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())