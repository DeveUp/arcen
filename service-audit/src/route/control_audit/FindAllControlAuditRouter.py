from fastapi import APIRouter

from src.service.control_audit.FindAllControlAuditService import FindAllControlAuditService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_CONTROL_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_ALL

router_find_all_control_audit = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_CONTROL_AUDIT_CLOSURE+ENDPOINT_GENERIC_FIND_ALL

@router_find_all_control_audit.get(endpoint)
async def find_all():
    service = FindAllControlAuditService()
    return service.execute(dict())