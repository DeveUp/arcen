from fastapi import APIRouter

from src.model.entity.ClosureAudit import ClosureAudit as EntityArcen

from src.service.audit_closure.FindByIdAuditClosureService import FindByIdAuditClosureService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_find_by_id_audit_closure = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit_closure']['path']+ENDPOINT['service']['audit_closure']['operation']['get']['find_by_id']
response = EntityArcen
status = RESPONSE['audit_closure']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['audit_closure']['column'][0]

# @Rest - Consulta una auditoria de cierre de una tabla
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_by_id_audit_closure.get(endpoint, response_model = response, status_code= status)
async def find_by_id(table:str, id:str):
    data = dict({info_data:id})
    service = ServiceArcen(table)
    return service.execute(data)