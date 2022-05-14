from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.service.audit.UpdateAuditService import UpdateAuditService

router_update_audit = APIRouter()

@router_update_audit.put("/{id}")
async def update(id: str, audit: AuditDto):
    data = dict({
        'id': id, 
        'audit': audit
    })
    service = UpdateAuditService()
    return service.execute(data)