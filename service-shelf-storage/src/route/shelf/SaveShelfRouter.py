from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ShelfDto import ShelfDto
from src.model.response.ShelfResponse import ShelfResponse as ResponseArcen
from src.service.shelf.SaveShelfService import SaveShelfService as ServiceArcen
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF, ENDPOINT_APP, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_SAVE,RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_shelf.post(endpoint, status_code=status,tags=["Shelf"])
async def save(shelf: ShelfDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_SHELF: shelf})
    service = ServiceArcen(db)
    return service.execute(data)