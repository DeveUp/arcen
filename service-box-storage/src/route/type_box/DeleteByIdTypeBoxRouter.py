"""
    @name - DeleteByIdTypeBoxRouter
    @description - Punto de entrada servicio type box operacion eliminar type box por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends, Response
from http import HTTPStatus

from sqlalchemy.orm import Session

from src.service.type_box.DeleteByIdTypeBoxService import DeleteByIdTypeBoxService as DeleteService
from src.persistence.database.table.TypeBoxTable import TypeBoxTable as TableArcen
from src.util.constant import COLUMN_TYPE_BOX_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_BOX,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_BOX+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE

# @Rest - Elimina un type box por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_type_box.delete(endpoint,status_code=status,tags=["Type_Box"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_BOX_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)