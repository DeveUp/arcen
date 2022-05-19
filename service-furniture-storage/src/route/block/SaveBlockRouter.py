from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BlockDto import BlockDto
from src.service.block.SaveBlockService import SaveBlockService
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_SAVE

router_save_block = APIRouter()
table = TableArcen()

@router_save_block.post(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_SAVE)
async def save(block: BlockDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BLOCK: block})
    service = SaveBlockService(db)
    return service.execute(data)