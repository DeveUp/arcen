from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.shelf.FindAllShelfService import FindAllShelfService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_shelf = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_shelf.get(ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_FIND_ALL,status_code=status)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllShelfService(db)
    return service.execute(dict())