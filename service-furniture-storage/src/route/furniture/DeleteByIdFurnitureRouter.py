from fastapi import APIRouter

from src.service.furniture.DeleteByIdFurnitureService import DeleteByIdFurnitureService
from src.util.constant import COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_furniture = APIRouter()

@router_detele_by_id_furniture.delete(ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str):
    data = dict({COLUMN_FURNITURE_ID:id})
    service = DeleteByIdFurnitureService()
    return service.execute(data)