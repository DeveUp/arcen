"""
    @name - SaveBuildingRouter
    @description - Punto de entrada servicio edificio operacion registrar un edificio
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

from src.service.building.SaveBuildingService import SaveBlockService as ServiceArcen

from src.persistence.database.table.BuildingTable import BuildingTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_building = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['building']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['building']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['building']['name']

# @Rest - Registra un edificio
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<BuildingResponse>
@router_save_building.post(endpoint, response_model = response, status_code= status)
async def save(element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)