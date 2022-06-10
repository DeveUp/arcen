from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ShelfDto import ShelfDto
from src.model.response.ShelfResponse import ShelfResponse as ResponseArcen
from src.service.shelf.UpdateShelfService import UpdateShelfService as ServiceArcen
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF, COLUMN_SHELF_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_UPDATE

router_update_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_shelf.put(endpoint,response_model = response,status_code=status,tags=["Shelf"])
async def update(id: str, shelf: ShelfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_SHELF_ID: id, 
        COLUMN_SHELF: shelf
    })
    service = ServiceArcen(db)
    return service.execute(data)