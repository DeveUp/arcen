"""
    @name - UpdateTypeFurnitureRouter
    @description - Punto de entrada servicio tipo de mueble operacion actualizar un tipo de mueble por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.model.response.TypeFurnitureResponse import TypeFurnitureResponse as ResponseArcen

from src.service.type_furniture.UpdateTypeFurnitureService import UpdateTypeFurnitureService as ServiceArcen

from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_furniture']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['type_furniture']['put']['update']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['type_furniture']['name']
info_data_pk = DATABASE['table']['type_furniture']['pk']

# @Rest - Actualiza un tipo de mueble por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeFurnitureResponse>
@router_update_type_furniture.put(endpoint, response_model = response, status_code= status)
async def update(id: str, type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: type_furniture
    })
    service = ServiceArcen(db)
    return service.execute(data)