from fastapi import APIRouter

from src.service.type_furniture.FindByIdTypeFurnitureService import FindByIdTypeFurnitureService
from src.util.constant import COLUMN_TYPE_FURNITURE_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_type_furniture = APIRouter()

@router_find_by_id_type_furniture.get(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str):
    data = dict({COLUMN_TYPE_FURNITURE_ID_TWO:id})
    service = FindByIdTypeFurnitureService()
    return service.execute(data)