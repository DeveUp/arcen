from fastapi import APIRouter

from src.service.audit.FindAllAuditService import FindAllAuditService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_audit = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['audit']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['audit']['get']['find_all']['response']
status = RESPONSE['audit']['get']['find_all']['success']['default']['code']

@router_find_all_audit.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())