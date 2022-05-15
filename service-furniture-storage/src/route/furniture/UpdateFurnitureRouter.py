from fastapi import APIRouter

from src.model.dto.FurnitureDto import FurnitureDto
from src.service.furniture.UpdateFurnitureService import UpdateFurnitureService
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_UPDATE

router_update_furniture = APIRouter()

@router_update_furniture.put(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, furniture: FurnitureDto):
    data = dict({
        COLUMN_FURNITURE_ID_TWO: id, 
        COLUMN_FURNITURE: furniture
    })
    service = UpdateFurnitureService()
    return service.execute(data)