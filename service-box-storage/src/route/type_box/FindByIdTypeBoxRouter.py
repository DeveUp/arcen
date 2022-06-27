"""
    @name - FindByIdTypeBoxRouter
    @description - Punto de entrada servicio type box operacion consulta un type box por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.TypeBoxResponse import TypeBoxResponse as ResponseArcen
from src.service.type_box.FindByIdTypeBoxService import FindByIdTypeBoxService as ServiceArcen
from src.persistence.database.table.TypeBoxTable import TypeBoxTable as TableArcen
from src.util.constant import COLUMN_TYPE_BOX_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_TYPE_BOX, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_type_box = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_BOX+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

# @Rest - Consulta un type box por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeBox>
@router_find_by_id_type_box.get(endpoint,response_model=response,status_code=status,tags=["Type_Box"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_BOX_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)