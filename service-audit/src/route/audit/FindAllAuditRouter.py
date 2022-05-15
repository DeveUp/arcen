from fastapi import APIRouter

from src.service.audit.FindAllAuditService import FindAllAuditService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_ALL

router_find_all_audit = APIRouter()

@router_find_all_audit.get(ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_ALL)
async def find_all():
    service = FindAllAuditService()
    return service.execute(dict())