from fastapi import APIRouter

from src.model.dto.DocumentLocationDto import DocumentLocationDto as DtoArcen
from src.model.entity.DocumentLocation import DocumentLocation as EntityArcen

from src.service.document_location.SaveDocumentLocationService import SaveDocumentLocationService as ServiceArcen

from src.util.constant import COLUMN_DOCUMENT_LOCATION, ENDPOINT_APP, ENDPOINT_APP_DOCUMENT_LOCATION, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_document_location = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT_LOCATION+ENDPOINT_GENERIC_SAVE
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_document_location.post(endpoint, response_model = response, status_code= status)
async def save(element: DtoArcen):
    data = dict({COLUMN_DOCUMENT_LOCATION: element})
    service = ServiceArcen()
    return service.execute(data)