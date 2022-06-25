"""
    @name - UpdateUserRoleRouter
    @description - Punto de entrada servicio user role operacion actualizar un user role por su pk
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
from src.service.UserRole.UpdateUserRoleService import UpdateUserRoleService as ServiceArcen
from src.persistence.database.table.UserRoleTable import UserRoleTable as TableArcen
from src.util.constant import COLUMN_USER_ROLE, COLUMN_USER_ROLE_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_USER_ROLE, ENDPOINT_GENERIC_UPDATE

router_update_user_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER_ROLE+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

# @Rest - Actualiza un user role por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<UserRole>
@router_update_user_role.put(endpoint ,response_model = response ,status_code=status,tags=["UserRole"])
async def update(id: str, userRole: UserRoleDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_USER_ROLE_ID: id, 
        COLUMN_USER_ROLE: userRole
    })
    service = ServiceArcen(db)
    return service.execute(data)