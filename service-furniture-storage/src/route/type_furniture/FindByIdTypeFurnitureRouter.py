from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.FindByIdTypeFurnitureService import FindByIdTypeFurnitureService
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_type_furniture = APIRouter()
table = TableArcen()

@router_find_by_id_type_furniture.get(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_FURNITURE_ID:id})
    service = FindByIdTypeFurnitureService(db)
    return service.execute(data)