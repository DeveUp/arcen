from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.service.type_furniture.UpdateTypeFurnitureService import UpdateTypeFurnitureService
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_UPDATE

router_update_type_furniture = APIRouter()
table = TableArcen()

@router_update_type_furniture.put(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_FURNITURE_ID: id, 
        COLUMN_TYPE_FURNITURE: type_furniture
    })
    service = UpdateTypeFurnitureService(db)
    return service.execute(data)