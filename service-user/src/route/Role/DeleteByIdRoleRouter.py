"""
    @name - DeleteByIdRoleRouter
    @description - Punto de entrada servicio role operacion eliminar role por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends, Response
from http import HTTPStatus
from sqlalchemy.orm import Session

from src.service.role.DeleteByIdRoleService import DeleteByIdRoleService as ServiceArcen
from src.persistence.database.table.RoleTable import RoleTable as TableArcen
from src.util.constant import COLUMN_ROLE_ID, ENDPOINT_APP, ENDPOINT_APP_ROLE, ENDPOINT_GENERIC_DELETE_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

router_detele_by_id_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_ROLE+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

# @Rest - Elimina un role por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_role.delete(endpoint, status_code= status,tags=["Role"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_ROLE_ID:id})
    service = ServiceArcen(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)