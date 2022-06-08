from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.TypeShelfResponse import TypeShelfResponse as ResponseArcen
from src.service.type_shelf.FindByIdTypeShelfService import FindByIdTypeShelfService as ServiceArcen
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_type_shelf = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_type_shelf.get(endpoint,response_model=response,status_code=status,tags=["TypeShelf"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_SHELF_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)