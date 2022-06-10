from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BoxDto import BoxDto
from src.model.response.BoxResponse import BoxResponse as ResponseArcen
from src.service.box.UpdateBoxService import UpdateBoxService as ServiceArcen
from src.persistence.database.table.BoxTable import BoxTable as TableArcen
from src.util.constant import COLUMN_BOX, COLUMN_BOX_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_BOX, ENDPOINT_GENERIC_UPDATE

router_update_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BOX+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_box.put(endpoint ,response_model = response ,status_code=status,tags=["Box"])
async def update(id: str, box: BoxDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_BOX_ID: id, 
        COLUMN_BOX: box
    })
    service = ServiceArcen(db)
    return service.execute(data)