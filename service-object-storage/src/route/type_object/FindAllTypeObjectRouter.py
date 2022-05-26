from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_object.FindAllTypeObjectService import FindAllTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_TYPE_OBJECT, ENDPOINT_GENERIC_FIND_ALL

router_find_all_type_object = APIRouter()
table = TableArcen()

@router_find_all_type_object.get(ENDPOINT_APP+ENDPOINT_APP_TYPE_OBJECT+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())