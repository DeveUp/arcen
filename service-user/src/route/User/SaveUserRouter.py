from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.UserDto import UserDto
from src.model.response.UserResponse import UserResponse as ResponseArcen
from src.service.user.SaveUserService import SaveUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import COLUMN_USER, ENDPOINT_APP, ENDPOINT_APP_USER, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_user = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_user.post(endpoint, response_model = response, status_code= status,tags=["User"])
async def save(user: UserDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER: user})
    service = ServiceArcen(db)
    return service.execute(data)