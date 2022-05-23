from fastapi import APIRouter

from src.model.dto.ClosureAuditDto import ClosureAuditDto
from src.service.audit_closure.SaveAuditClosureService import SaveAuditClosureService
from src.util.constant import COLUMN_AUDIT_CLOSURE_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_SAVE

router_save_audit_closure = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_GENERIC_SAVE

@router_save_audit_closure.post(endpoint)
async def save(audit_closure: ClosureAuditDto):
    data = dict({COLUMN_AUDIT_CLOSURE_NAME: audit_closure})
    service = SaveAuditClosureService()
    return service.execute(data)