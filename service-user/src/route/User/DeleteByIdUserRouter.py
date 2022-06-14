from fastapi import APIRouter, Depends, Response
from http import HTTPStatus
from sqlalchemy.orm import Session

from src.service.user.DeleteByIdUserService import DeleteByIdUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import COLUMN_USER_ID, ENDPOINT_APP, ENDPOINT_APP_USER, ENDPOINT_GENERIC_DELETE_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

router_detele_by_id_user = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID

@router_detele_by_id_user.delete(endpoint, status_code= status,tags=["User"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER_ID:id})
    service = ServiceArcen(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)