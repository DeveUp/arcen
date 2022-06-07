from fastapi import APIRouter

from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService as ServiceArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_BY_RANGE_DATE
from src.util.constant import COLUMN_AUDIT_DATE_START, COLUMN_AUDIT_DATE_END
from src.util.constant import RESPONSE_MODEL_AUDIT_FIND_ALL_BY_RANGE_DATE, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE

router_find_all_by_range_date_creation_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_BY_RANGE_DATE
response = RESPONSE_MODEL_AUDIT_FIND_ALL_BY_RANGE_DATE
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE

@router_find_all_by_range_date_creation_audit.get(endpoint, response_model = response, status_code= status)
async def find_all_by_range_date_creation(start:str, end:str):
    data = dict({
        COLUMN_AUDIT_DATE_START:start,
        COLUMN_AUDIT_DATE_END: end
    })
    service = ServiceArcen()
    return service.execute(data)