"""
    @name - FindAllFurnitureRouter
    @description - Punto de entrada servicio mueble operacion consultar todos los muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.furniture.FindAllFurnitureService import FindAllFurnitureService as ServiceArcen

from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['furniture']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['furniture']['get']['find_all']['response']
status = RESPONSE['furniture']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todos muebles
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_furniture.get(endpoint, response_model= response, status_code= status)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())