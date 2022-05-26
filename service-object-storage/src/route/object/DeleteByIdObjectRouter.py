from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.object.DeleteByIdObjectService import DeleteByIdObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen
from src.util.constant import COLUMN_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_OBJECT, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_object = APIRouter()
table = TableArcen()

@router_detele_by_id_object.delete(ENDPOINT_APP+ENDPOINT_APP_OBJECT+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_OBJECT_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)