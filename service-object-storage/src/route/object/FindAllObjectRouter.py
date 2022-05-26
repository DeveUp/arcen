from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.object.FindAllObjectService import FindAllObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_OBJECT, ENDPOINT_GENERIC_FIND_ALL

router_find_all_object = APIRouter()
table = TableArcen()

@router_find_all_object.get(ENDPOINT_APP+ENDPOINT_APP_OBJECT+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())