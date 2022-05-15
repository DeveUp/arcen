from fastapi import APIRouter

from src.service.block.FindByIdBlockService import FindByIdBlockService
from src.util.constant import COLUMN_BLOCK_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_block = APIRouter()

@router_find_by_id_block.get(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str):
    data = dict({COLUMN_BLOCK_ID_TWO:id})
    service = FindByIdBlockService()
    return service.execute(data)