from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.FurnitureResponse import FurnitureResponse as ResponseArcen
from src.service.furniture.FindByIdFurnitureService import FindByIdFurnitureService as ServiceArcen
from src.persistence.database.table.FurnitureTable import FurnitureTable as TableArcen
from src.util.constant import COLUMN_FURNITURE_ID, ENDPOINT_APP, ENDPOINT_APP_FURNITURE, ENDPOINT_GENERIC_FIND_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

router_find_by_id_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_FURNITURE+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_furniture.get(endpoint, response_model = response, status_code= status)
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_FURNITURE_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)