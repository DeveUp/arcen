from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ShelfDto import ShelfDto
from src.service.shelf.UpdateShelfService import UpdateShelfService
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF, COLUMN_SHELF_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_UPDATE

router_update_shelf = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_shelf.put(ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_UPDATE,status_code=status)
async def update(id: str, shelf: ShelfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_SHELF_ID: id, 
        COLUMN_SHELF: shelf
    })
    service = UpdateShelfService(db)
    return service.execute(data)