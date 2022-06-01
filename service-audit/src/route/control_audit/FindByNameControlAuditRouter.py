from fastapi import APIRouter

from src.model.entity.ControlAudit import ControlAudit
from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService as ServiceArcen
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME_NAME, ENDPOINT_APP, ENDPOINT_APP_CONTROL_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_BY_NAME
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME

router_find_by_name_control_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_CONTROL_AUDIT_CLOSURE+ENDPOINT_GENERIC_FIND_BY_NAME
response = ControlAudit
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME

@router_find_by_name_control_audit.get(endpoint, response_model = response, status_code= status)
async def find_by_name(name:str):
    data = dict({COLUMN_CONTROL_AUDIT_NAME_NAME:name})
    service = ServiceArcen()
    return service.execute(data)