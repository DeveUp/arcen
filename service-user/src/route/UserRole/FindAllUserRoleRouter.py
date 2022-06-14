from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.UserRole.FindAllUserRoleService import FindAllUserRoleService as ServiceArcen
from src.persistence.database.table.UserRoleTable import UserRoleTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_USER_ROLE, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_GENERIC_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_user_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER_ROLE+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_GENERIC_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_user_role.get(endpoint, response_model = response, status_code= status,tags=["UserRole"])
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())