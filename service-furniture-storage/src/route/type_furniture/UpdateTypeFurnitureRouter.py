from fastapi import APIRouter

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.service.type_furniture.UpdateTypeFurnitureService import UpdateTypeFurnitureService
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_UPDATE

router_update_type_furniture = APIRouter()

@router_update_type_furniture.put(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, type_furniture: TypeFurnitureDto):
    data = dict({
        COLUMN_TYPE_FURNITURE_ID: id, 
        COLUMN_TYPE_FURNITURE: type_furniture
    })
    service = UpdateTypeFurnitureService()
    return service.execute(data)