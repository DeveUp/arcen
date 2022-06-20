"""
    @name - UpdateTypeObjectRouter
    @description - Punto de entrada servicio tipo de objeto operacion actualizar un tipo de objeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeObjectDto import TypeObjectDto as DtoArcen
from src.model.response.TypeObjectResponse import TypeObjectResponse as ResponseArcen

from src.service.type_object.UpdateTypeObjectService import UpdateTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_type_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_object']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['type_object']['put']['update']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['type_object']['name']
info_data_pk = DATABASE['table']['type_object']['pk']

# @Rest - Actualiza un tipo de objeto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeObject>
@router_update_type_object.put(endpoint, response_model=response,status_code= status)
async def update(id: str, type_object: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: type_object
    })
    service = ServiceArcen(db)
    return service.execute(data)