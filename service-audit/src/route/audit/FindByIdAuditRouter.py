from fastapi import APIRouter

from src.model.entity.Audit import Audit as EntityArcen

from src.service.audit.FindByIdAuditService import FindByIdAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_id_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit']['path']+ENDPOINT['operation']['get']['find_by_id']
response = EntityArcen
status = RESPONSE['audit']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['audit']['column'][0]

# @Rest - Consulta una auditoria por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_by_id_audit.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str):
    data = dict({info_data:id})
    service = ServiceArcen()
    return service.execute(data)