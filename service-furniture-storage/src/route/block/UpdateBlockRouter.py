from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BlockDto import BlockDto
from src.service.block.UpdateBlockService import UpdateBlockService
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_UPDATE

router_update_block = APIRouter()
table = TableArcen()

@router_update_block.put(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, block: BlockDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_BLOCK_ID: id, 
        COLUMN_BLOCK: block
    })
    service = UpdateBlockService()
    return service.execute(data)