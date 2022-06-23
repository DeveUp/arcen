"""
    @name - UpdateBuildingRouter
    @description - Punto de entrada servicio edificio operacion actualizar un edificio por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BuildingDto import BuildingDto as DtoArcen
from src.model.response.BuildingResponse import BuildingResponse as ResponseArcen

from src.service.building.UpdateBuildingService import UpdateBuildingService as ServiceArcen

from src.persistence.database.table.BuildingTable import BuildingTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_building = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['building']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['building']['put']['update']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['building']['name']
info_data_pk = DATABASE['table']['building']['pk']

# @Rest - Actualiza un edificio por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<BuildingResponse>
@router_update_building.put(endpoint, response_model = response, status_code= status)
async def update(id: str, element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)