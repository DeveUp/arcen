"""
    @name - FindByIdFurnitureRouter
    @description - Punto de entrada servicio mueble operacion consulta un mueble por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.FurnitureResponse import FurnitureResponse as ResponseArcen

from src.service.furniture.FindByIdFurnitureService import FindByIdFurnitureService as ServiceArcen

from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_id_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['furniture']['path']+ENDPOINT['operation']['get']['find_by_id']
response = ResponseArcen
status = RESPONSE['furniture']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['furniture']['column'][0]

# @Rest - Consulta un mueble por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Furniture>
@router_find_by_id_furniture.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({
        info_data:id
    })
    service = ServiceArcen(db)
    return service.execute(data)