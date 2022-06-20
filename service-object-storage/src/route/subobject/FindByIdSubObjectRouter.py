"""
    @name - FindByIdObjectRouter
    @description - Punto de entrada servicio subobjeto operacion consulta un subobjeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.SubObjectResponse import SubObjectResponse as ResponseArcen

from src.service.subobject.FindByIdSubObjectService import FindByIdSubObjectService as ServiceArcen

from src.persistence.database.table.SubObjectTable import SubObjectTable as TableArcen 

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_id_subobject = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['subobject']['path']+ENDPOINT['operation']['get']['find_by_id']
response = ResponseArcen
status = RESPONSE['subobject']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['subobject']['column'][0]

# @Rest - Consulta un subobjeto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<SubObjectResponse>
@router_find_by_id_subobject.get(endpoint, response_model=response, status_code= status)
async def find_by_id(id:str, db:Session=Depends(table.execute)):
    data = dict({
        info_data:id
    })
    service = ServiceArcen(db)
    return service.execute(data)