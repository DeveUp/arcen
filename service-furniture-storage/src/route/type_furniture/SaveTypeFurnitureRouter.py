"""
    @name - SaveTypeFurnitureRouter
    @description - Punto de entrada servicio tipo de mueble operacion registrar un tipo de mueble
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

from src.service.type_furniture.SaveTypeFurnitureService import SaveTypeFurnitureService as ServiceArcen

from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_furniture']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['type_furniture']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['type_furniture']['name']

# @Rest - Registra un tipo de mueble
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeFurnitureResponse>
@router_save_type_furniture.post(endpoint, response_model = response, status_code= status)
async def save(type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        info_data: type_furniture
    })
    service = ServiceArcen(db)
    return service.execute(data)