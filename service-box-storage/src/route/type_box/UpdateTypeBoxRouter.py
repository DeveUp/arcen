from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeBoxDto import TypeBoxfDto
from src.model.response.TypeBoxResponse import TypeBoxResponse as ResponseArcen
from src.service.type_box.UpdateTypeBoxService import UpdateTypeBoxService as ServiceArcen
from src.persistence.database.table.TypeBoxTable import TypeBoxTable as TableArcen
from src.util.constant import COLUMN_TYPE_BOX, COLUMN_TYPE_BOX_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_TYPE_BOX, ENDPOINT_GENERIC_UPDATE

router_update_type_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_BOX+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_type_box.put(endpoint ,response_model = response ,status_code=status,tags=["Type_Box"])
async def update(id: str, type_box: TypeBoxfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_BOX_ID: id, 
        COLUMN_TYPE_BOX: type_box
    })
    service = ServiceArcen(db)
    return service.execute(data)