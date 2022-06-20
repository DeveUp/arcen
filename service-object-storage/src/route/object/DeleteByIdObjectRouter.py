"""
    @name - DeleteByIdObjectRouter
    @description - Punto de entrada servicio objecto operacion eliminar objecto por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.object.DeleteByIdObjectService import DeleteByIdObjectService as ServiceArcen

from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_detele_by_id_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['object']['path']+ENDPOINT['operation']['delete']['delete_by_id']
status = RESPONSE['object']['delete']['delete_by_id']['success']['default']['code']
info_data = DATABASE['table']['object']['column'][0]

# @Rest - Elimina un objecto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_object.delete(endpoint, status_code= status)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({info_data:id})
    service = ServiceArcen(db)
    service.execute(data)