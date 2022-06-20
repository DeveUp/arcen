"""
    @name - UpdateObjectRouter
    @description - Punto de entrada servicio objecto operacion actualizar un objecto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ObjectDto import ObjectDto as DtoArcen
from src.model.response.ObjectResponse import ObjectResponse as ResponseEntity

from src.service.object.UpdateObjectService import UpdateObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['object']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['object']['put']['update']['success']['default']['code']
response = ResponseEntity
info_data = DATABASE['table']['object']['name']
info_data_pk = DATABASE['table']['object']['pk']

# @Rest - Actualiza un objecto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Object>
@router_update_object.put(endpoint, response_model=response,status_code= status)
async def update(id: str, block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: block
    })
    service = ServiceArcen(db)
    return service.execute(data)