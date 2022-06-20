"""
    @name - UpdateSubObjectRouter
    @description - Punto de entrada servicio subobjeto operacion actualizar un subobjeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.SubObjectDto import SubObjectDto as DtoArcen
from src.model.response.SubObjectResponse import SubObjectResponse as ResponseArcen

from src.service.subobject.UpdateSubObjectService import UpdateSubObjectService as ServiceArcen
from src.persistence.database.table.SubObjectTable import SubObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_subobject = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['subobject']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['subobject']['put']['update']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['subobject']['name']
info_data_pk = DATABASE['table']['subobject']['pk']

# @Rest - Actualiza un subobjeto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<SubObjectResponse>
@router_update_subobject.put(endpoint, response_model=response,status_code= status)
async def update(id: str, element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)