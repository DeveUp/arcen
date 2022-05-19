from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.block.FindByIdBlockService import FindByIdBlockService
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_block = APIRouter()
table = TableArcen()

@router_find_by_id_block.get(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_BY_ID)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BLOCK_ID:id})
    service = FindByIdBlockService(db)
    return service.execute(data)