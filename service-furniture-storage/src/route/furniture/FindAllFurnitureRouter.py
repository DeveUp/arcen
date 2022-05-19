from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.furniture.FindAllFurnitureService import FindAllFurnitureService
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_ALL

router_find_all_furniture = APIRouter()
table = TableArcen()

@router_find_all_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllFurnitureService(db)
    return service.execute(dict())