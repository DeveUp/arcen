from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeObjectDto import TypeObjectDto as DtoArcen
from src.service.type_object.SaveTypeObjectService import SaveTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen
from src.util.constant import COLUMN_TYPE_OBJECT, ENDPOINT_APP, ENDPOINT_APP_TYPE_OBJECT, ENDPOINT_GENERIC_SAVE

router_save_type_object = APIRouter()
table = TableArcen()

@router_save_type_object.post(ENDPOINT_APP+ENDPOINT_APP_TYPE_OBJECT+ENDPOINT_GENERIC_SAVE)
async def save(block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_OBJECT: block})
    service = ServiceArcen(db)
    return service.execute(data)