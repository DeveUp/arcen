from fastapi import APIRouter

from src.model.entity.ControlAudit import ControlAudit as EntityArcen
from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_find_by_name_control_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['control_audit']['path']+ENDPOINT['operation']['get']['find_by_name']
response = EntityArcen
status = RESPONSE['control_audit']['get']['find_by_name']['success']['default']['code']
info_data = DATABASE['table']['control_audit']['column'][1]

# @Rest - Consulta un control de auditoria por su nombre
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_by_name_control_audit.get(endpoint, response_model = response, status_code= status)
async def find_by_name(name:str):
    data = dict({info_data:name})
    service = ServiceArcen()
    return service.execute(data)