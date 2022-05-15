from fastapi import APIRouter

from src.service.furniture.FindAllFurnitureService import FindAllFurnitureService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_ALL

router_find_all_furniture = APIRouter()

@router_find_all_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_ALL)
async def find_all():
    service = FindAllFurnitureService()
    return service.execute(dict())