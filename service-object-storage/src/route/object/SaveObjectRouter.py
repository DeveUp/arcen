from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ObjectDto import ObjectDto as DtoArcen
from src.service.object.SaveObjectService import SaveObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen
from src.util.constant import COLUMN_OBJECT, ENDPOINT_APP, ENDPOINT_APP_OBJECT, ENDPOINT_GENERIC_SAVE

router_save_object = APIRouter()
table = TableArcen()

@router_save_object.post(ENDPOINT_APP+ENDPOINT_APP_OBJECT+ENDPOINT_GENERIC_SAVE)
async def save(block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({COLUMN_OBJECT: block})
    service = ServiceArcen(db)
    return service.execute(data)