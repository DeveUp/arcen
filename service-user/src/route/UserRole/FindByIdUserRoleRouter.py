from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.UserRoleResponse import UserRoleResponse as ResponseArcen
from src.service.UserRole import FindByIdUserRoleService as ServiceArcen
from src.persistence.database.table.UserRoleTable import UserRoleTable as TableArcen
from src.util.constant import COLUMN_USER_ROLE_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_USER_ROLE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_user_role = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_USER_ROLE+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_user_role.get(endpoint,response_model=response,status_code=status,tags=["UserRole"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER_ROLE_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)