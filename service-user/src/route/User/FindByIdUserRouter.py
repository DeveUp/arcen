from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.model.response.UserResponse import UserResponse as ResponseArcen
from src.service.user.FindByIdUserService import FindByIdUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import COLUMN_USER_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_APP_USER, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_user = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_USER+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_user.get(endpoint,response_model=response,status_code=status,tags=["User"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)