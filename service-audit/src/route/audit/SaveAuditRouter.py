from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.service.audit.SaveAuditService import SaveAuditService
from src.util.constant import COLUMN_AUDIT_NAME

router_save_audit = APIRouter()

@router_save_audit.post("/")
async def save(audit: AuditDto):
    data = dict({COLUMN_AUDIT_NAME: audit})
    service = SaveAuditService()
    return service.execute(data)