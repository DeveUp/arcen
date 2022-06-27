"""
    @name - DeleteByIdShelfRouter
    @description - Punto de entrada servicio shelf operacion eliminar shelf por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends, Response
from http import HTTPStatus

from sqlalchemy.orm import Session

from src.service.shelf.DeleteByIdShelfService import DeleteByIdShelfService as DeleteService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF_ID, ENDPOINT_APP, ENDPOINT_APP_SHELF,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_DELETE_BY_ID
status=RESPONSE_STATUS_CODE_GENERIC_DELETE

# @Rest - Elimina un shelf por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_shelf.delete(endpoint,status_code=status,tags=["Shelf"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_SHELF_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)