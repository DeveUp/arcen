from fastapi import APIRouter

from src.service.block.FindAllBlockService import FindAllBlockService
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_ALL

router_find_all_block = APIRouter()

@router_find_all_block.get(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_ALL)
async def find_all():
    service = FindAllBlockService()
    return service.execute(dict())