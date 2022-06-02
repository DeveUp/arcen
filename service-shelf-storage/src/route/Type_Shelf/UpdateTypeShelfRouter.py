from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeShelfDto import TypeShelfDto
from src.service.type_shelf.UpdateTypeShelfService import UpdateTypeShelfService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF, COLUMN_TYPE_SHELF_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_UPDATE

router_update_type_shelf = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_type_shelf.put(ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_UPDATE,status_code=status)
async def update(id: str, type_shelf: TypeShelfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_SHELF_ID: id, 
        COLUMN_TYPE_SHELF: type_shelf
    })
    service = UpdateTypeShelfService(db)
    return service.execute(data)