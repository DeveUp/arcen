from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.DependenceDto import DependenceDto
from src.model.response.DependenceResponse import DependenceResponse as ResponseArcen
from src.service.dependence.SaveDependenceService import SaveDependenceService as ServiceArcen
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE, ENDPOINT_APP, ENDPOINT_APP_DEPENDENCE,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_GENERIC_SAVE

router_save_dependence = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_dependence.post(endpoint, response_model = response, status_code=status ,tags=["Dependence"])
async def save(dependence: DependenceDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_DEPENDENCE: dependence})
    service = ServiceArcen(db)
    return service.execute(data)