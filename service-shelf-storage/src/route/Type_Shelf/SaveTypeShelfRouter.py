from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeShelfDto import TypeShelfDto
from src.service.type_shelf.SaveTypeShelfService import SaveTypeShelfService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF, ENDPOINT_APP, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_SAVE

router_save_type_shelf = APIRouter()
table = TableArcen()

@router_save_type_shelf.post(ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_SAVE)
async def save(type_shelf: TypeShelfDto, db: Session = Depends(table.execute)):
    #print(type_shelf)
    data = dict({COLUMN_TYPE_SHELF: type_shelf})
    service = SaveTypeShelfService(db)
    return service.execute(data)