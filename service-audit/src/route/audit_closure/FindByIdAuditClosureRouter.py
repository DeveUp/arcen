from fastapi import APIRouter

from src.service.audit_closure.FindByIdAuditClosureService import FindByIdAuditClosureService
from src.util.constant import COLUMN_AUDIT_ID_TWO_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_BY_ID, ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID

router_find_by_id_audit_closure = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID+ENDPOINT_GENERIC_FIND_BY_ID

@router_find_by_id_audit_closure.get(endpoint)
async def find_by_id(table:str, id:str):
    data = dict({COLUMN_AUDIT_ID_TWO_NAME:id})
    service = FindByIdAuditClosureService(table)
    return service.execute(data)