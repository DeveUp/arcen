from fastapi import APIRouter

from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_BY_RANGE_DATE
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME

router_find_all_by_range_date_creation_audit = APIRouter()
endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_BY_RANGE_DATE

@router_find_all_by_range_date_creation_audit.get(endpoint)
async def find_all_by_range_date_creation(start:str, end:str):
    data = dict({
        COLUMN_AUDIT_DATE_START_NAME:start,
        COLUMN_AUDIT_DATE_END_NAME: end
    })
    service = FindAllByRangeDateCreationAuditService()
    return service.execute(data)