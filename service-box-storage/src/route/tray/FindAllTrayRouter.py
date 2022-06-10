from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.tray.FindAllTrayService import FindAllTrayService as FindAllService
from src.persistence.database.table.TrayTable import TrayTable as TableArcen
from src.util.constant import ENDPOINT_APP,RESPONSE_MODEL_TRAY_FIND_ALL, ENDPOINT_APP_TRAY, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_tray = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_TRAY+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_TRAY_FIND_ALL
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_tray.get(endpoint,response_model=response,status_code=status,tags=["Tray"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())