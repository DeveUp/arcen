"""
    @name - UpdateBlockRouter
    @description - Punto de entrada servicio bloque operacion actualizar un bloque por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BlockDto import BlockDto as DtoArcen
from src.model.response.BlockResponse import BlockResponse as ResponseArcen

from src.service.block.UpdateBlockService import UpdateBlockService as ServiceArcen

from src.persistence.database.table.BlockTable import BlockTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_update_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['block']['path']+ENDPOINT['operation']['put']['update']
status = RESPONSE['block']['put']['update']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['block']['name']
info_data_pk = DATABASE['table']['block']['pk']

# @Rest - Actualiza un bloque por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<BlockResponse>
@router_update_block.put(endpoint, response_model = response, status_code= status)
async def update(id: str, element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data_pk: id, 
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)