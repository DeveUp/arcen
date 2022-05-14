from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.service.audit.SaveAuditService import SaveAuditService

router_save_audit = APIRouter()

@router_save_audit.post("/")
async def save(audit: AuditDto):
    data = dict(audit=audit)
    return SaveAuditService.execute(data)