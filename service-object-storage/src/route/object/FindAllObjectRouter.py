"""
    @name - FindAllObjectRouter
    @description - Punto de entrada servicio objecto operacion consultar todos los objectos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.object.FindAllObjectService import FindAllObjectService as ServiceArcen

from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE

router_find_all_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['object']['path']+ENDPOINT['operation']['get']['find_all']
response = RESPONSE['object']['get']['find_all']['response']
status = RESPONSE['object']['get']['find_all']['success']['default']['code']

# @Rest - Consulta todos objectos
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objecto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_object.get(endpoint, response_model = response, status_code= status)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())