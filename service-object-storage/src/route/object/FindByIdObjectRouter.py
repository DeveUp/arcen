from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.object.FindByIdObjectService import FindByIdObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen
from src.util.constant import COLUMN_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_OBJECT, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_object = APIRouter()
table = TableArcen()

@router_find_by_id_object.get(ENDPOINT_APP+ENDPOINT_APP_OBJECT+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_OBJECT_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)