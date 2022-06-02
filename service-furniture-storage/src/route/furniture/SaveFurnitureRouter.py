from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.FurnitureDto import FurnitureDto
from src.model.request.FurnitureRequest import FurnitureRequest
from src.service.furniture.SaveFurnitureService import SaveFurnitureService as ServiceArcen
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_SAVE
response = FurnitureRequest
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_furniture.post(endpoint, response_model = response, status_code= status)
async def save(furniture: FurnitureDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_FURNITURE: furniture})
    service = ServiceArcen(db)
    return service.execute(data)