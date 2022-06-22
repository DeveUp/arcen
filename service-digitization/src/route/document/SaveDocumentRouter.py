"""
    @description - Ruta del servicio documento operacion registrar documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter

from src.model.dto.DocumentDto import DocumentDto as DtoArcen
from src.model.entity.Document import Document as EntityArcen

from src.service.document.SaveDocumentService import SaveDocumentService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_save_document = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['document']['path']+ENDPOINT['operation']['post']['save']
response = EntityArcen
status = RESPONSE['document']['post']['save']['success']['default']['code']
info_data = DATABASE['table']['document']['name']

# @Rest - Registra una documento
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Document>
@router_save_document.post(endpoint, response_model = response, status_code= status)
async def save(audit: DtoArcen):
    data = dict({info_data: audit})
    service = ServiceArcen()
    return service.execute(data)