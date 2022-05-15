from fastapi import APIRouter

from src.service.audit.FindByIdAuditService import FindByIdAuditService
from src.util.constant import COLUMN_AUDIT_ID_TWO_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_audit = APIRouter()

@router_find_by_id_audit.get(ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str):
    data = dict({COLUMN_AUDIT_ID_TWO_NAME:id})
    service = FindByIdAuditService()
    return service.execute(data)