"""
    @name - SaveUserRoleRouter
    @description - Punto de entrada servicio user role operacion registrar un user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.UserRoleDto import UserRoleDto
from src.model.response.UserRoleResponse import UserRoleResponse as ResponseArcen
from src.service.UserRole.SaveUserRoleService import SaveUserRoleService as ServiceArcen
from src.persistence.database.table.UserRoleTable import UserRoleTable as TableArcen
from src.util.constant import COLUMN_USER_ROLE, ENDPOINT_APP, ENDPOINT_APP_USER_ROLE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_user_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER_ROLE+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

# @Rest - Registra un user role
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<UserRole>
@router_save_user_role.post(endpoint, response_model = response, status_code= status,tags=["UserRole"])
async def save(userRole: UserRoleDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER_ROLE: userRole})
    service = ServiceArcen(db)
    return service.execute(data)