from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.shelf.FindByIdShelfService import FindByIdShelfService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF_ID, ENDPOINT_APP, ENDPOINT_APP_SHELF,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_shelf = APIRouter()
table = TableArcen()
status= RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_shelf.get(ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_FIND_BY_ID,status_code=status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_SHELF_ID:id})
    service = FindByIdShelfService(db)
    return service.execute(data)