from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.shelf.FindAllShelfService import FindAllShelfService as FindAllService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_FIND_ALL
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_shelf.get(endpoint,status_code=status,tags=["Shelf"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())