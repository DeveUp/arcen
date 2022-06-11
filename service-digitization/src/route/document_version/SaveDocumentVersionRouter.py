from fastapi import APIRouter

from src.model.dto.DocumentVersionDto import DocumentVersionDto as DtoArcen
from src.model.entity.DocumentVersion import DocumentVersion as EntityArcen

from src.service.document_version.SaveDocumentVersionService import SaveDocumentVersionService as ServiceArcen

from src.util.constant import COLUMN_DOCUMENT_VERSION, ENDPOINT_APP, ENDPOINT_APP_DOCUMENT_VERSION, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_document_version = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT_VERSION+ENDPOINT_GENERIC_SAVE
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_document_version.post(endpoint, response_model = response, status_code= status)
async def save(element: DtoArcen):
    data = dict({COLUMN_DOCUMENT_VERSION: element})
    service = ServiceArcen()
    return service.execute(data)