from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto
from src.model.entity.Audit import Audit
from src.service.audit.SaveAuditService import SaveAuditService as ServiceArcen
from src.util.constant import COLUMN_AUDIT, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_SAVE
response = Audit
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_audit.post(endpoint, response_model = response, status_code= status)
async def save(audit: AuditDto):
    data = dict({COLUMN_AUDIT: audit})
    service = ServiceArcen()
    return service.execute(data)