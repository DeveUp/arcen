from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.block.DeleteByIdBlockService import DeleteByIdBlockService
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_block = APIRouter()
table = TableArcen()

@router_detele_by_id_block.delete(ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_DELETE_BY_ID)
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BLOCK_ID:id})
    service = DeleteByIdBlockService(db)
    return service.execute(data)