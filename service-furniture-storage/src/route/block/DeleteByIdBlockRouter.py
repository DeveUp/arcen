"""
    @name - DeleteByIdBlockRouter
    @description - Punto de entrada servicio bloque operacion eliminar bloque por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.block.DeleteByIdBlockService import DeleteByIdBlockService as ServiceArcen

from src.persistence.database.table.BlockTable import BlockTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_detele_by_id_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['block']['path']+ENDPOINT['operation']['delete']['delete_by_id']
status = RESPONSE['block']['delete']['delete_by_id']['success']['default']['code']
info_data = DATABASE['table']['block']['column'][0]

# @Rest - Elimina un objeto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_block.delete(endpoint, status_code= status)
async def delete_by_id(id: str, db:Session= Depends(table.execute)):
    data = dict({info_data:id})
    service = ServiceArcen(db)
    service.execute(data)