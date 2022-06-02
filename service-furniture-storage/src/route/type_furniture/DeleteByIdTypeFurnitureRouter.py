from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.DeleteByIdTypeFurnitureService import DeleteByIdTypeFurnitureService as ServiceArcen
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_DELETE_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

router_detele_by_id_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

@router_detele_by_id_type_furniture.delete(endpoint, status_code= status)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_FURNITURE_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)