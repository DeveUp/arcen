from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.response.DependenceResponse import DependenceResponse as ResponseArcen
from src.service.dependence.FindByIdDependenceService import FindByIdDependenceService as ServiceArcen
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE_ID, ENDPOINT_APP, ENDPOINT_APP_DEPENDENCE,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID, ENDPOINT_GENERIC_FIND_BY_ID

router_find_by_id_dependence = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_FIND_BY_ID
response = ResponseArcen
status= RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID

@router_find_by_id_dependence.get(endpoint, response_model=response,status_code=status,tags=["Dependence"])
async def find_by_id(id:str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_DEPENDENCE_ID:id})
    service = ServiceArcen(db)
    return service.execute(data)