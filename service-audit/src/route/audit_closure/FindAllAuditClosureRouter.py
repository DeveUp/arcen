from fastapi import APIRouter

from src.service.audit_closure.FindAllAuditClosureService import FindAllAuditClosureService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_ALL, ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID

router_find_all_audit_closure = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID+ENDPOINT_GENERIC_FIND_ALL

@router_find_all_audit_closure.get(endpoint)
async def find_all(table:str):
    service = FindAllAuditClosureService(table)
    return service.execute(dict())