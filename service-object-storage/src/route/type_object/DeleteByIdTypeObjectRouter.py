from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_object.DeleteByIdTypeObjectService import DeleteByIdTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen
from src.util.constant import COLUMN_TYPE_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_OBJECT, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_object = APIRouter()
table = TableArcen()

@router_detele_by_id_type_object.delete(ENDPOINT_APP+ENDPOINT_APP_TYPE_OBJECT+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_OBJECT_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)