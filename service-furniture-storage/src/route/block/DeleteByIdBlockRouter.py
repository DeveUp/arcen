from fastapi import APIRouter

from src.service.block.DeleteByIdBlockService import DeleteByIdBlockService
from src.util.constant import COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_block = APIRouter()

@router_detele_by_id_block.delete(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str):
    data = dict({COLUMN_BLOCK_ID:id})
    service = DeleteByIdBlockService()
    return service.execute(data)