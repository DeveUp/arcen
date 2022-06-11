from fastapi import APIRouter

from src.model.dto.DocumentDto import DocumentDto as DtoArcen
from src.model.entity.Document import Document as EntityArcen
from src.service.document.SaveDocumentService import SaveDocumentService as ServiceArcen
from src.util.constant import COLUMN_DOCUMENT, ENDPOINT_APP, ENDPOINT_APP_DOCUMENT, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_document = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DOCUMENT+ENDPOINT_GENERIC_SAVE
response = EntityArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_document.post(endpoint, response_model = response, status_code= status)
async def save(audit: DtoArcen):
    data = dict({COLUMN_DOCUMENT: audit})
    service = ServiceArcen()
    return service.execute(data)