from fastapi import APIRouter

from src.service.control_audit.FindByIdControlAuditService import FindByIdControlAuditService
from src.util.constant import COLUMN_AUDIT_ID_TWO_NAME, ENDPOINT_APP, ENDPOINT_APP_CONTROL_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_control_audit = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_CONTROL_AUDIT_CLOSURE+ENDPOINT_GENERIC_FIND_BY_ID

@router_find_by_id_control_audit.get(endpoint)
async def find_by_id(id:str):
    data = dict({COLUMN_AUDIT_ID_TWO_NAME:id})
    service = FindByIdControlAuditService()
    return service.execute(data)