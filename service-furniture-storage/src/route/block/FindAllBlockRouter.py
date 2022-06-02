from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.block.FindAllBlockService import FindAllBlockService as ServiceArcen
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_BLOCK_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_BLOCK_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_block.get(endpoint, response_model = response, status_code= status)
async def find_all(db: Session = Depends(table.execute)):
    service = ServiceArcen(db)
    return service.execute(dict())