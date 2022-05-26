from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ObjectDto import ObjectDto as DtoArcen
from src.service.object.UpdateObjectService import UpdateObjectService as ServiceArcen
from src.persistence.database.table.ObjectTable import ObjectTable as TableArcen
from src.util.constant import COLUMN_OBJECT, COLUMN_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_OBJECT, ENDPOINT_GENERIC_UPDATE

router_update_object = APIRouter()
table = TableArcen()

@router_update_object.put(ENDPOINT_APP+ENDPOINT_APP_OBJECT+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_OBJECT_ID: id, 
        COLUMN_OBJECT: block
    })
    service = ServiceArcen(db)
    return service.execute(data)