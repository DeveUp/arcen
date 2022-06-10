from fastapi import APIRouter, Depends, Response
from http import HTTPStatus

from sqlalchemy.orm import Session

from src.service.tray.DeleteByIdTrayService import DeleteByIdTrayService as DeleteService
from src.persistence.database.table.TrayTable import TrayTable as TableArcen
from src.util.constant import COLUMN_TRAY_ID, ENDPOINT_APP, ENDPOINT_APP_TRAY,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_tray = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TRAY+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE

@router_detele_by_id_tray.delete(endpoint,status_code=status,tags=["Tray"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TRAY_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)