from fastapi import APIRouter

from src.model.dto.BlockDto import BlockDto
from src.service.block.SaveBlockService import SaveBlockService
from src.util.constant import COLUMN_BLOCK, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_SAVE

router_save_block = APIRouter()

@router_save_block.post(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_SAVE)
async def save(block: BlockDto):
    data = dict({COLUMN_BLOCK: block})
    service = SaveBlockService()
    return service.execute(data)