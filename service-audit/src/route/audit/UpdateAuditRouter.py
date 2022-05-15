from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.service.audit.UpdateAuditService import UpdateAuditService
from src.util.constant import COLUMN_AUDIT_NAME, COLUMN_AUDIT_ID_TWO_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_UPDATE

router_update_audit = APIRouter()

@router_update_audit.put(ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, audit: AuditDto):
    data = dict({
        COLUMN_AUDIT_ID_TWO_NAME: id, 
        COLUMN_AUDIT_NAME: audit
    })
    service = UpdateAuditService()
    return service.execute(data)