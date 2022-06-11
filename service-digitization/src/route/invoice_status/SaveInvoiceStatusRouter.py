from fastapi import APIRouter

from src.model.dto.InvoiceStatusDto import InvoiceStatusDto as DtoArcen
from src.model.entity.InvoiceStatus import InvoiceStatus as EntityArcen

from src.service.invoice_status.SaveInvoiceStatusService import SaveInvoiceStatusService as ServiceArcen

from src.util.constant import COLUMN_INVOICE_STATUS, ENDPOINT_APP, ENDPOINT_APP_INVOICE_STATUS, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_invoice_status = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_INVOICE_STATUS+ENDPOINT_GENERIC_SAVE
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_invoice_status.post(endpoint, response_model = response, status_code= status)
async def save(element: DtoArcen):
    data = dict({COLUMN_INVOICE_STATUS: element})
    service = ServiceArcen()
    return service.execute(data)