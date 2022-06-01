from fastapi import APIRouter

from src.model.entity.Audit import Audit
from src.service.audit.FindByIdAuditService import FindByIdAuditService as ServiceArcen
from src.util.constant import COLUMN_AUDIT_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_BY_ID
response = Audit
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_audit.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str):
    data = dict({COLUMN_AUDIT_ID_TWO:id})
    service = ServiceArcen()
    return service.execute(data)