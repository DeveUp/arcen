from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BlockDto import BlockDto
from src.model.request.BlockRequest import BlockRequest
from src.service.block.SaveBlockService import SaveBlockService as ServiceArcen
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_SAVE
response = BlockRequest
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_block.post(endpoint, response_model = response, status_code= status)
async def save(block: BlockDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BLOCK: block})
    service = ServiceArcen(db)
    return service.execute(data)