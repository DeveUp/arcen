from fastapi import APIRouter, Depends, Response
from http import HTTPStatus

from sqlalchemy.orm import Session

from src.service.dependence.DeleteByIdDependenceService import DeleteByIdDependenceService as DeleteService
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE_ID, ENDPOINT_APP, ENDPOINT_APP_DEPENDENCE,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_dependence = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE

@router_detele_by_id_dependence.delete(endpoint,status_code=status,tags=["Dependence"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_DEPENDENCE_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)