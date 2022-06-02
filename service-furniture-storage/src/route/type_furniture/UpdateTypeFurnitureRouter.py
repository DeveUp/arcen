from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.model.request.TypeFurnitureRequest import TypeFurnitureRequest
from src.service.type_furniture.UpdateTypeFurnitureService import UpdateTypeFurnitureService as ServiceArcen
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_UPDATE

router_update_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_UPDATE
response = TypeFurnitureRequest
status = RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_type_furniture.put(endpoint, response_model = response, status_code= status)
async def update(id: str, type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_FURNITURE_ID: id, 
        COLUMN_TYPE_FURNITURE: type_furniture
    })
    service = ServiceArcen(db)
    return service.execute(data)