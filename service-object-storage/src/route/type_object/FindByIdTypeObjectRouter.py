"""
    @name - FindByIdTypeObjectRouter
    @description - Punto de entrada servicio tipo de objeto operacion consulta un tipo de objeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.TypeObjectResponse import TypeObjectResponse as ResponseArcen

from src.service.type_object.FindByIdTypeObjectService import FindByIdTypeObjectService as ServiceArcen

from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_id_type_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_object']['path']+ENDPOINT['operation']['get']['find_by_id']
response = ResponseArcen
status = RESPONSE['type_object']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['type_object']['column'][0]

# @Rest - Consulta un tipo de objeto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeObject>
@router_find_by_id_type_object.get(endpoint, response_model=response, status_code= status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({
        info_data:id
    })
    service = ServiceArcen(db)
    return service.execute(data)