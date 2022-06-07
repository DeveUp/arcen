from fastapi import APIRouter

from src.service.control_audit.FindAllControlAuditService import FindAllControlAuditService as ServiceArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_CONTROL_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_CONTROL_AUDIT_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_control_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_CONTROL_AUDIT_CLOSURE+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_CONTROL_AUDIT_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_control_audit.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())