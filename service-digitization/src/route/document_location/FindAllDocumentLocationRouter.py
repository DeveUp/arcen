from fastapi import APIRouter

from src.service.document_location.FindAllDocumentLocationService import FindAllDocumentLocationService as ServiceArcen

from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_DOCUMENT_LOCATION, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_DOCUMENT_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_document_location = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT_LOCATION+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_DOCUMENT_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_document_location.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())