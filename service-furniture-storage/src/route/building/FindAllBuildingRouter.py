"""
    @name - FindAllBuildingRouter
    @description - Punto de entrada servicio edificio operacion consultar todos los edificios
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.building.FindAllBuildingService import FindAllBuildingService as ServiceArcen

from src.persistence.database.table.BuildingTable import BuildingTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_building = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['building']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['building']['get']['find_all']['response']
status = RESPONSE['building']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todos edificios
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_building.get(endpoint, response_model = response, status_code= status)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())