from fastapi import APIRouter

from src.model.dto.BlockDto import BlockDto
from src.service.block.UpdateBlockService import UpdateBlockService
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID_TWO, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_UPDATE

router_update_block = APIRouter()

@router_update_block.put(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, block: BlockDto):
    data = dict({
        COLUMN_BLOCK_ID_TWO: id, 
        COLUMN_BLOCK: block
    })
    service = UpdateBlockService()
    return service.execute(data)