from fastapi import APIRouter

from src.service.audit_closure.FindAllAuditClosureService import FindAllAuditClosureService as ServiceArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_ALL, ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID
from src.util.constant import RESPONSE_MODEL_CLOSURE_AUDIT_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_audit_closure = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_CLOSURE_AUDIT_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_audit_closure.get(endpoint, response_model = response, status_code= status)
async def find_all(table:str):
    service = ServiceArcen(table)
    return service.execute(dict())