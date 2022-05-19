from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.block.FindAllBlockService import FindAllBlockService
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_ALL

router_find_all_block = APIRouter()
table = TableArcen()

@router_find_all_block.get(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_ALL)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllBlockService(db)
    return service.execute(dict())