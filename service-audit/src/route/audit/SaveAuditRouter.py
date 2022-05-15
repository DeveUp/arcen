from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.service.audit.SaveAuditService import SaveAuditService
from src.util.constant import COLUMN_AUDIT_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_SAVE

router_save_audit = APIRouter()

@router_save_audit.post(ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_SAVE)
async def save(audit: AuditDto):
    data = dict({COLUMN_AUDIT_NAME: audit})
    service = SaveAuditService()
    return service.execute(data)