from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.furniture.FindByIdFurnitureService import FindByIdFurnitureService
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_furniture = APIRouter()
table = TableArcen()

@router_find_by_id_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_FURNITURE_ID:id})
    service = FindByIdFurnitureService(db)
    return service.execute(data)