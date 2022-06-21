"""
    @name - SaveFurnitureRouter
    @description - Punto de entrada servicio mueble operacion registrar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.FurnitureDto import FurnitureDto as DtoArcen
from src.model.response.FurnitureResponse import FurnitureResponse as ResponseArcen

from src.service.furniture.SaveFurnitureService import SaveFurnitureService as ServiceArcen

from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['furniture']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['furniture']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['furniture']['name']

# @Rest - Registra un mueble
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<FurnitureResponse>
@router_save_furniture.post(endpoint, response_model = response, status_code= status)
async def save(element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)