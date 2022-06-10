from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.TrayResponse import TrayResponse as ResponseArcen
from src.service.tray.FindByIdTrayService import FindByIdTrayService as ServiceArcen
from src.persistence.database.table.TrayTable import TrayTable as TableArcen
from src.util.constant import COLUMN_TRAY_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_TRAY, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_tray = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TRAY+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_tray.get(endpoint,response_model=response,status_code=status,tags=["Tray"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TRAY_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)