from fastapi import APIRouter

from src.service.audit_closure.FindAllAuditClosureService import FindAllAuditClosureService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_audit_closure = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit_closure']['path']+ENDPOINT['service']['audit_closure']['operation']['get']['find_all']
response = RESPONSE['audit_closure']['get']['find_all']['response']
status = RESPONSE['audit_closure']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todas las auditoria de cierre de una tabla
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_all_audit_closure.get(endpoint, response_model = response, status_code= status)
async def find_all(table:str):
    service = ServiceArcen(table)
    return service.execute(dict())