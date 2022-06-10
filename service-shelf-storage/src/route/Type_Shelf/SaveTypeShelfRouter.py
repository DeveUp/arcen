from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeShelfDto import TypeShelfDto
from src.model.response.TypeShelfResponse import TypeShelfResponse as ResponseArcen
from src.service.type_shelf.SaveTypeShelfService import SaveTypeShelfService as ServiceArcen
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_SAVE

router_save_type_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_type_shelf.post(endpoint, response_model = response,status_code=status,tags=["TypeShelf"])
async def save(type_shelf: TypeShelfDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_SHELF: type_shelf})
    service = ServiceArcen(db)
    return service.execute(data)