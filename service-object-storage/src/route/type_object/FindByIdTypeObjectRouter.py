from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_object.FindByIdTypeObjectService import FindByIdTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen
from src.util.constant import COLUMN_TYPE_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_OBJECT, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_type_object = APIRouter()
table = TableArcen()

@router_find_by_id_type_object.get(ENDPOINT_APP+ENDPOINT_APP_TYPE_OBJECT+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_OBJECT_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)