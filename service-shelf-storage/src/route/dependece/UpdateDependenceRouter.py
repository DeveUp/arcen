from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.DependenceDto import DependenceDto
from src.model.response.DependenceResponse import DependenceResponse as ResponseArcen
from src.service.dependence.UpdateDependenceService import UpdateDependenceService as ServiceArcen
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE, COLUMN_DEPENDENCE_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP_DEPENDENCE, ENDPOINT_GENERIC_UPDATE

router_update_dependence = APIRouter()
table = TableArcen()
endpoint = ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_dependence.put(endpoint, response_model = response, status_code=status,tags=["Dependence"])
async def update(id: str, dependence: DependenceDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_DEPENDENCE_ID: id, 
        COLUMN_DEPENDENCE: dependence
    })
    service = ServiceArcen(db)
    return service.execute(data)