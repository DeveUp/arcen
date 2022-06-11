from fastapi import APIRouter

from src.model.entity.DocumentLocation import DocumentLocation as EntityArcen

from src.service.document_location.FindByIdDocumentLocationService import FindByIdDocumentLocationService as ServiceArcen

from src.util.constant import COLUMN_DOCUMENT_LOCATION_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_DOCUMENT_LOCATION, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_document_location = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT_LOCATION+ENDPOINT_GENERIC_FIND_BY_ID
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_document_location.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str):
    data = dict({COLUMN_DOCUMENT_LOCATION_ID_TWO:id})
    service = ServiceArcen()
    return service.execute(data)