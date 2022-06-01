from fastapi import APIRouter

from src.model.entity.ClosureAudit import ClosureAudit
from src.service.audit_closure.FindByIdAuditClosureService import FindByIdAuditClosureService as ServiceArcen
from src.util.constant import COLUMN_AUDIT_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_FIND_BY_ID, ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_audit_closure = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID+ENDPOINT_GENERIC_FIND_BY_ID
response = ClosureAudit
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_audit_closure.get(endpoint, response_model = response, status_code= status)
async def find_by_id(table:str, id:str):
    data = dict({COLUMN_AUDIT_ID_TWO:id})
    service = ServiceArcen(table)
    return service.execute(data)