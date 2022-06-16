from fastapi import APIRouter

from src.model.dto.ClosureAuditDto import ClosureAuditDto as DtoArcen

from src.service.audit_closure.SaveAuditClosureService import SaveAuditClosureService

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_audit_closure = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit_closure']['path']+ENDPOINT['operation']['post']['save']
response = RESPONSE['audit_closure']['post']['save']['success']['default']['code']
status = RESPONSE['audit_closure']['post']['save']['response']
info_data = DATABASE['table']['audit_closure']['name']

# @Rest - Registra una auditoria de cierre
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_save_audit_closure.post(endpoint, response_model = response, status_code= status)
async def save(audit_closure: DtoArcen):
    data = dict({info_data: audit_closure})
    service = SaveAuditClosureService()
    return service.execute(data)