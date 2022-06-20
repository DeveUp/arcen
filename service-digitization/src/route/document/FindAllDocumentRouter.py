"""
    @description - Ruta del servicio documento operacion consultar todos los documentos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter

from src.service.document.FindAllDocumentService import FindAllDocumentService as ServiceArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_document = APIRouter()

endpoint = ENDPOINT['path']+ENDPOINT['service']['document']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['document']['get']['find_all']['response']
status = RESPONSE['document']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todas los documentos
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_document.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())