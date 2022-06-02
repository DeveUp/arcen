from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.furniture.DeleteByIdFurnitureService import DeleteByIdFurnitureService
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_DELETE_BY_ID
from src.util.constant import RESPONSE_MODEL_FURNITURE_DELETE_BY_ID

router_detele_by_id_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_MODEL_FURNITURE_DELETE_BY_ID

@router_detele_by_id_furniture.delete(endpoint, status_code= status)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_FURNITURE_ID:id})
    service = DeleteByIdFurnitureService(db)
    return service.execute(data)