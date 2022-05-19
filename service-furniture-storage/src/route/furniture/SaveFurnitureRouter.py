from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.FurnitureDto import FurnitureDto
from src.service.furniture.SaveFurnitureService import SaveFurnitureService
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_SAVE

router_save_furniture = APIRouter()
table = TableArcen()

@router_save_furniture.post(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_SAVE)
async def save(furniture: FurnitureDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_FURNITURE: furniture})
    service = SaveFurnitureService(db)
    return service.execute(data)