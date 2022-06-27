"""
    @name - FindByIdBlockRouter
    @description - Punto de entrada servicio bloque operacion consulta un bloque por su letra y piso
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.BlockResponse import BlockResponse as ResponseArcen

from src.service.block.FindByLetterAndFlatBlockService import FindByLetterAndFlatBlockService as ServiceArcen

from src.persistence.database.table.BlockTable import BlockTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_letter_and_flat_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['block']['path']+ENDPOINT['service']['block']['operation']['get']['find_by_letter_and_flat']
response = ResponseArcen
status = RESPONSE['block']['get']['find_by_letter_and_flat']['success']['default']['code']
info_data_letter = DATABASE['table']['block']['column'][1]
info_data_flat = DATABASE['table']['block']['column'][2]

# @Rest - Consulta un bloque por su letra y piso
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Block>
@router_find_letter_and_flat_block.get(endpoint, response_model = response, status_code= status)
async def find_by_id(letter:str, flat:str, db: Session= Depends(table.execute)):
    data = dict({
        info_data_letter:letter,
        info_data_flat:flat
    })
    service = ServiceArcen(db)
    return service.execute(data)