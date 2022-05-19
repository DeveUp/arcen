from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.FindAllTypeFurnitureService import FindAllTypeFurnitureService
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_ALL

router_find_all_type_furniture = APIRouter()
table = TableArcen()

@router_find_all_type_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllTypeFurnitureService(db)
    return service.execute(dict())