"""
    @name - FindAllTypeFurnitureRouter
    @description - Punto de entrada servicio tipo de mueble operacion consultar todos los tipo de muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.FindAllTypeFurnitureService import FindAllTypeFurnitureService as ServiceArcen
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_furniture']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['type_furniture']['get']['find_all']['response']
status = RESPONSE['type_furniture']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todos tipos de muebles
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_type_furniture.get(endpoint, response_model = response, status_code= status)
async def find_all(db:Session= Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())