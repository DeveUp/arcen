from fastapi import APIRouter

from src.model.entity.InvoiceStatus import InvoiceStatus as EntityArcen

from src.service.invoice_status.FindByIdInvoiceStatusService import FindByIdInvoiceStatusService as ServiceArcen

from src.util.constant import COLUMN_DOCUMENT_VERSION_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_INVOICE_STATUS, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_invoice_status = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_INVOICE_STATUS+ENDPOINT_GENERIC_FIND_BY_ID
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_invoice_status.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str):
    data = dict({COLUMN_DOCUMENT_VERSION_ID_TWO:id})
    service = ServiceArcen()
    return service.execute(data)