from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.service.type_furniture.SaveTypeFurnitureService import SaveTypeFurnitureService
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_SAVE

router_save_type_furniture = APIRouter()
table = TableArcen()

@router_save_type_furniture.post(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_SAVE)
async def save(type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_FURNITURE: type_furniture})
    service = SaveTypeFurnitureService(db)
    return service.execute(data)