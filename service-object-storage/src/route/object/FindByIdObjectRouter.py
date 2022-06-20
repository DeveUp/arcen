"""
    @name - FindByIdObjectRouter
    @description - Punto de entrada servicio objecto operacion consulta un objecto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.entity.Object import Object as EntityArcen

from src.service.object.FindByIdObjectService import FindByIdObjectService as ServiceArcen

from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_find_by_id_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['object']['path']+ENDPOINT['operation']['get']['find_by_id']
response = EntityArcen
status = RESPONSE['object']['get']['find_by_id']['success']['default']['code']
info_data = DATABASE['table']['object']['column'][0]

# @Rest - Consulta un objecto por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Object>
@router_find_by_id_object.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({info_data:id})
    service = ServiceArcen(db)
    return service.execute(data)