from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.BlockResponse import BlockResponse as ResponseArcen
from src.service.block.FindByIdBlockService import FindByIdBlockService as ServiceArcen
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_block.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BLOCK_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)