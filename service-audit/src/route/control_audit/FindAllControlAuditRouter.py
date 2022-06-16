from fastapi import APIRouter

from src.service.control_audit.FindAllControlAuditService import FindAllControlAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_control_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['control_audit']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['control_audit']['get']['find_all']['response']
status = RESPONSE['control_audit']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todas los controles de auditoria
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_all_control_audit.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())