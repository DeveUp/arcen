from fastapi import APIRouter

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.service.type_furniture.SaveTypeFurnitureService import SaveTypeFurnitureService
from src.util.constant import COLUMN_TYPE_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_SAVE

router_save_type_furniture = APIRouter()

@router_save_type_furniture.post(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_SAVE)
async def save(type_furniture: TypeFurnitureDto):
    data = dict({COLUMN_TYPE_FURNITURE: type_furniture})
    service = SaveTypeFurnitureService()
    return service.execute(data)