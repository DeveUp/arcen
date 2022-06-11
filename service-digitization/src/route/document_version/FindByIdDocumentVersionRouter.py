from fastapi import APIRouter

from src.model.entity.DocumentVersion import DocumentVersion as EntityArcen

from src.service.document_version.FindByIdDocumentVersionService import FindByIdDocumentVersionService as ServiceArcen

from src.util.constant import COLUMN_DOCUMENT_VERSION_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_DOCUMENT_VERSION, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_document_version = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT_VERSION+ENDPOINT_GENERIC_FIND_BY_ID
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_document_version.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str):
    data = dict({COLUMN_DOCUMENT_VERSION_ID_TWO:id})
    service = ServiceArcen()
    return service.execute(data)