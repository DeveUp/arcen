from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.DependenceDto import DependenceDto
from src.service.dependence.UpdateDependenceService import UpdateDependenceService
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE, COLUMN_DEPENDENCE_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP_DEPENDENCE, ENDPOINT_GENERIC_UPDATE

router_update_dependence = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_dependence.put(ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_UPDATE,status_code=status)
async def update(id: str, dependence: DependenceDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_DEPENDENCE_ID: id, 
        COLUMN_DEPENDENCE: dependence
    })
    service = UpdateDependenceService(db)
    return service.execute(data)