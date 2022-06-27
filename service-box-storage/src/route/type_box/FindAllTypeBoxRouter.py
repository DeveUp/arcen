"""
    @name - FindAllTypeBoxRouter
    @description - Punto de entrada servicio type box operacion consultar todos los type box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_box.FindAllTypeBoxService import FindAllTypeBoxService as FindAllService
from src.persistence.database.table.TypeBoxTable import TypeBoxTable as TableArcen
from src.util.constant import ENDPOINT_APP,RESPONSE_MODEL_TYPE_BOX_FIND_ALL, ENDPOINT_APP_TYPE_BOX, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_type_box = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_BOX+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_TYPE_BOX_FIND_ALL
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

# @Rest - Consulta todos los type box
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<list>
@router_find_all_type_box.get(endpoint,response_model=response,status_code=status,tags=["Type_Box"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())