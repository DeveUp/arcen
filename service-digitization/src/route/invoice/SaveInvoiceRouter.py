from fastapi import APIRouter

from src.model.dto.InvoiceDto import InvoiceDto as DtoArcen
from src.model.entity.Invoice import Invoice as EntityArcen

from src.service.invoice.SaveInvoiceService import SaveInvoiceService as ServiceArcen

from src.util.constant import COLUMN_INVOICE, ENDPOINT_APP, ENDPOINT_APP_INVOICE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_invoice= APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_INVOICE+ENDPOINT_GENERIC_SAVE
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_invoice.post(endpoint, response_model = response, status_code= status)
async def save(element: DtoArcen):
    data = dict({COLUMN_INVOICE: element})
    service = ServiceArcen()
    return service.execute(data)