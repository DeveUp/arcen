from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.RoleDto import RoleDto
from src.model.response.RoleResponse import RoleResponse as ResponseArcen
from src.service.role.SaveRoleService import SaveRoleService as ServiceArcen
from src.persistence.database.table.RoleTable import RoleTable as TableArcen
from src.util.constant import COLUMN_ROLE, ENDPOINT_APP, ENDPOINT_APP_ROLE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_ROLE+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_role.post(endpoint, response_model = response, status_code= status,tags=["Role"])
async def save(role: RoleDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_ROLE: role})
    service = ServiceArcen(db)
    return service.execute(data)