from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_shelf.DeleteByIdTypeShelfService import DeleteByIdTypeShelfService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_shelf = APIRouter()
table = TableArcen()

@router_detele_by_id_type_shelf.delete(ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_SHELF_ID:id})
    service = DeleteByIdTypeShelfService(db)
    return service.execute(data)