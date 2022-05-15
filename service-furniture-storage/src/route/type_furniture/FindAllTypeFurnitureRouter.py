from fastapi import APIRouter

from src.service.type_furniture.FindAllTypeFurnitureService import FindAllTypeFurnitureService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_ALL

router_find_all_type_furniture = APIRouter()

@router_find_all_type_furniture.get(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_ALL)
async def find_all():
    service = FindAllTypeFurnitureService()
    return service.execute(dict())