from fastapi import APIRouter

from src.model.entity.ClosureAudit import ClosureAudit
from src.model.dto.ClosureAuditDto import ClosureAuditDto
from src.service.audit_closure.SaveAuditClosureService import SaveAuditClosureService
from src.util.constant import COLUMN_AUDIT_CLOSURE, ENDPOINT_APP, ENDPOINT_APP_AUDIT_CLOSURE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE, RESPONSE_MODEL_CLOSURE_AUDIT_SAVE

router_save_audit_closure = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT_CLOSURE+ENDPOINT_GENERIC_SAVE
response = RESPONSE_MODEL_CLOSURE_AUDIT_SAVE
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_audit_closure.post(endpoint, response_model = response, status_code= status)
async def save(audit_closure: ClosureAuditDto):
    data = dict({COLUMN_AUDIT_CLOSURE: audit_closure})
    service = SaveAuditClosureService()
    return service.execute(data)