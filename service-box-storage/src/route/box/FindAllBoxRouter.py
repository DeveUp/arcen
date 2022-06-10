from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.box.FindAllBoxService import FindAllBoxService as FindAllService
from src.persistence.database.table.BoxTable import BoxTable as TableArcen
from src.util.constant import ENDPOINT_APP,RESPONSE_MODEL_BOX_FIND_ALL, ENDPOINT_APP_BOX, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_box = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_BOX+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_BOX_FIND_ALL
status=RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_box.get(endpoint,response_model=response,status_code=status,tags=["Box"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())