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

@router_detele_by_id_shelf.delete(endpoint,status_code=status,tags=["Shelf"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_SHELF_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)