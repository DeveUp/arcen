from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ShelfDto import ShelfDto
from src.service.shelf.SaveShelfService import SaveShelfService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF, ENDPOINT_APP, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_SAVE,RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_shelf = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_shelf.post(ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_SAVE, status_code=status)
async def save(shelf: ShelfDto, db: Session = Depends(table.execute)):
    #print(shelf)
    data = dict({COLUMN_SHELF: shelf})
    service = SaveShelfService(db)
    return service.execute(data)