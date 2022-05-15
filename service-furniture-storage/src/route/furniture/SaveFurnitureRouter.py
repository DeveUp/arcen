from fastapi import APIRouter

from src.model.dto.FurnitureDto import FurnitureDto
from src.service.furniture.SaveFurnitureService import SaveFurnitureService
from src.util.constant import COLUMN_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_SAVE

router_save_furniture = APIRouter()

@router_save_furniture.post(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_SAVE)
async def save(furniture: FurnitureDto):
    data = dict({COLUMN_FURNITURE: furniture})
    service = SaveFurnitureService()
    return service.execute(data)