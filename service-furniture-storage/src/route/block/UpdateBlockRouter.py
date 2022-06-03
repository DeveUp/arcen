from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BlockDto import BlockDto
from src.model.response.BlockResponse import BlockResponse as ResponseArcen
from src.service.block.UpdateBlockService import UpdateBlockService as ServiceArcen
from src.persistence.database.table.BlockTable import BlockTable as TableArcen
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID, ENDPOINT_APP, ENDPOINT_APP_BLOCK, ENDPOINT_GENERIC_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_UPDATE

router_update_block = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BLOCK+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_block.put(endpoint, response_model = response, status_code= status)
async def update(id: str, block: BlockDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_BLOCK_ID: id, 
        COLUMN_BLOCK: block
    })
    service = ServiceArcen(db)
    return service.execute(data)