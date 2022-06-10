from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_shelf.FindAllTypeShelfService import FindAllTypeShelfService as FindAllService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import ENDPOINT_APP,RESPONSE_MODEL_TYPE_SHELF_FIND_ALL, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_type_shelf = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_TYPE_SHELF_FIND_ALL
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_type_shelf.get(endpoint,response_model=response,status_code=status,tags=["TypeShelf"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())