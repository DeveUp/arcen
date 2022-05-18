from fastapi import APIRouter

from src.service.furniture.FindByIdFurnitureService import FindByIdFurnitureService
from src.util.constant import COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_furniture = APIRouter()

@router_find_by_id_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str):
    data = dict({COLUMN_FURNITURE_ID:id})
    service = FindByIdFurnitureService()
    return service.execute(data)