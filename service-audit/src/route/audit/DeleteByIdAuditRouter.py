from fastapi import APIRouter

from src.service.audit.DeleteByIdAuditService import DeleteByIdAuditService
from src.util.constant import COLUMN_AUDIT_ID_TWO_NAME, ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_audit = APIRouter()

@router_detele_by_id_audit.delete(ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str):
    data = dict({COLUMN_AUDIT_ID_TWO_NAME:id})
    service = DeleteByIdAuditService()
    return service.execute(data)