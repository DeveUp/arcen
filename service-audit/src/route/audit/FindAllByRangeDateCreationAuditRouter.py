from fastapi import APIRouter

from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_find_all_by_range_date_creation_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit']['path']+ENDPOINT['operation']['get']['find_by_range_date_all']
response = RESPONSE['audit']['get']['find_by_range_date_all']['response']
status = RESPONSE['audit']['get']['find_by_range_date_all']['success']['default']['code']


# @Rest - Consulta todas las auditorias entre un rango de fechas
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response
@router_find_all_by_range_date_creation_audit.get(endpoint, response_model = response, status_code= status)
async def find_all_by_range_date_creation(start:str, end:str):
    length = len(DATABASE['table']['audit']['column']) - 1
    data = dict({
        DATABASE['table']['audit']['column'][length][0]:start,
        DATABASE['table']['audit']['column'][length][1]: end
    })
    service = ServiceArcen()
    return service.execute(data)