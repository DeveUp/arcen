from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_shelf.FindAllTypeShelfService import FindAllTypeShelfService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_FIND_ALL

router_find_all_type_shelf = APIRouter()
table = TableArcen()

@router_find_all_type_shelf.get(ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllTypeShelfService(db)
    return service.execute(dict())