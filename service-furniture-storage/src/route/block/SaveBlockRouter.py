"""
    @name - SaveBlockRouter
    @description - Punto de entrada servicio bloque operacion registrar un bloque
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

from src.service.block.SaveBlockService import SaveBlockService as ServiceArcen

from src.persistence.database.table.BlockTable import BlockTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['block']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['block']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['block']['name']

# @Rest - Registra un objeto
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<BlockResponse>
@router_save_block.post(endpoint, response_model = response, status_code= status)
async def save(element:DtoArcen, db:Session= Depends(table.execute)):
    data = dict({
        info_data: element
    })
    service = ServiceArcen(db)
    return service.execute(data)