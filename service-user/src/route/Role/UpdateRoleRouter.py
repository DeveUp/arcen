from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.RoleDto import RoleDto
from src.model.response.RoleResponse import RoleResponse as ResponseArcen
from src.service.role.UpdateRoleService import UpdateRoleService as ServiceArcen
from src.persistence.database.table.RoleTable import RoleTable as TableArcen
from src.util.constant import COLUMN_ROLE, COLUMN_ROLE_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_ROLE, ENDPOINT_GENERIC_UPDATE

router_update_role = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_ROLE+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_role.put(endpoint ,response_model = response ,status_code=status,tags=["Role"])
async def update(id: str, role: RoleDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_ROLE_ID: id, 
        COLUMN_ROLE: role
    })
    service = ServiceArcen(db)
    return service.execute(data)