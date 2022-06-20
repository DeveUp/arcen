"""
    @name - SaveObjectRouter
    @description - Punto de entrada servicio objecto operacion registrar un objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ObjectDto import ObjectDto as DtoArcen
from src.model.response.ObjectResponse import ObjectResponse as ResponseArcen

from src.service.object.SaveObjectService import SaveObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['object']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['object']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['object']['name']

# @Rest - Registra un objecto
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Object>
@router_save_object.post(endpoint, response_model = response, status_code= status)
async def save(block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        info_data: block
    })
    service = ServiceArcen(db)
    return service.execute(data)