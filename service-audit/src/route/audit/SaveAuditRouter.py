from fastapi import APIRouter

from src.model.dto.AuditDto import AuditDto as DtoArcen
from src.model.entity.Audit import Audit as EntityArcen

from src.service.audit.SaveAuditService import SaveAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit']['path']+ENDPOINT['operation']['post']['save']
response = EntityArcen
status = RESPONSE['audit', 'post', 'save', 'response']
info_data = DATABASE['table']['audit']['name']

@router_save_audit.post(endpoint, response_model = response, status_code= status)
async def save(audit: DtoArcen):
    data = dict({info_data: audit})
    service = ServiceArcen()
    return service.execute(data)