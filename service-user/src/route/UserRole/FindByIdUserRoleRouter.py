"""
    @name - FindByIdUserRoleRouter
    @description - Punto de entrada servicio user role operacion consulta un user role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.UserRoleResponse import UserRoleResponse as ResponseArcen
from src.service.UserRole.FindByIdUserRoleService import FindByIdUserRoleService as ServiceArcen
from src.persistence.database.table.UserRoleTable import UserRoleTable as TableArcen
from src.util.constant import COLUMN_USER_ROLE_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_USER_ROLE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_user_role = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_USER_ROLE+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

# @Rest - Consulta un user role por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<UserRole>
@router_find_by_id_user_role.get(endpoint,response_model=response,status_code=status,tags=["UserRole"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER_ROLE_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)