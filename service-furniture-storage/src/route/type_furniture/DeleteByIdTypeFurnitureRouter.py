from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.DeleteByIdTypeFurnitureService import DeleteByIdTypeFurnitureService
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_furniture = APIRouter()
table = TableArcen()

@router_detele_by_id_type_furniture.delete(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_FURNITURE_ID:id})
    service = DeleteByIdTypeFurnitureService(db)
    return service.execute(data)