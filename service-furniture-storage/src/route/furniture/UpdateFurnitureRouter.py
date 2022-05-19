from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.FurnitureDto import FurnitureDto
from src.service.furniture.UpdateFurnitureService import UpdateFurnitureService
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_UPDATE

router_update_furniture = APIRouter()
table = TableArcen()

@router_update_furniture.put(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, furniture: FurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_FURNITURE_ID: id, 
        COLUMN_FURNITURE: furniture
    })
    service = UpdateFurnitureService(db)
    return service.execute(data)