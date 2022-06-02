from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.FurnitureDto import FurnitureDto
from src.model.request.FurnitureRequest import FurnitureRequest
from src.service.furniture.UpdateFurnitureService import UpdateFurnitureService as ServiceArcen
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_UPDATE

router_update_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_UPDATE
response = FurnitureRequest
status = RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_furniture.put(endpoint, response_model = response, status_code= status)
async def update(id: str, furniture: FurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_FURNITURE_ID: id, 
        COLUMN_FURNITURE: furniture
    })
    service = ServiceArcen(db)
    return service.execute(data)