from fastapi import APIRouter

from src.service.type_furniture.DeleteByIdTypeFurnitureService import DeleteByIdTypeFurnitureService
from src.util.constant import COLUMN_TYPE_FURNITURE_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_furniture = APIRouter()

@router_detele_by_id_type_furniture.delete(ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str):
    data = dict({COLUMN_TYPE_FURNITURE_ID_TWO:id})
    service = DeleteByIdTypeFurnitureService()
    return service.execute(data)