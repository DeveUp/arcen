"""
    @name - FindByNameAndFlatBuildingRouter
    @description - Punto de entrada servicio edificio operacion consulta un edificio por un nombre y piso
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-27
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.BuildingResponse import BuildingResponse as ResponseArcen

from src.service.building.FindByNameAndFlatBuildingService import FindByNameAndFlatBuildingService as ServiceArcen

from src.persistence.database.table.BuildingTable import BuildingTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_name_and_flat_building = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['building']['path']+ENDPOINT['service']['building']['operation']['get']['find_by_name_and_flat']
response = ResponseArcen
status = RESPONSE['building']['get']['find_by_name_and_flat']['success']['default']['code']
info_data_name = DATABASE['table']['building']['column'][1]
info_data_flat = DATABASE['table']['building']['column'][4]

# @Rest - Consulta un edificio por su nombre y piso
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Building>
@router_find_by_name_and_flat_building.get(endpoint, response_model = response, status_code= status)
async def find_by_id(name:str, flat:str, db: Session= Depends(table.execute)):
    data = dict({
        info_data_name:name,
        info_data_flat:flat
    })
    service = ServiceArcen(db)
    return service.execute(data)