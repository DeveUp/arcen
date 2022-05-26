from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeObjectDto import TypeObjectDto as DtoArcen
from src.service.type_object.UpdateTypeObjectService import UpdateTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen
from src.util.constant import COLUMN_TYPE_OBJECT, COLUMN_TYPE_OBJECT_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_OBJECT, ENDPOINT_GENERIC_UPDATE

router_update_type_object = APIRouter()
table = TableArcen()

@router_update_type_object.put(ENDPOINT_APP+ENDPOINT_APP_TYPE_OBJECT+ENDPOINT_GENERIC_UPDATE)
async def update(id: str, type_object: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_OBJECT_ID: id, 
        COLUMN_TYPE_OBJECT: type_object
    })
    service = ServiceArcen(db)
    return service.execute(data)