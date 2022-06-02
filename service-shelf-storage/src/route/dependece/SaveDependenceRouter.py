from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.DependenceDto import DependenceDto
from src.service.dependence.SaveDependenceService import SaveDependenceService
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import COLUMN_DEPENDENCE, ENDPOINT_APP, ENDPOINT_APP_DEPENDENCE,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_GENERIC_SAVE

router_save_dependence = APIRouter()
table = TableArcen()
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_dependence.post(ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_SAVE,status_code=status)
async def save(type_shelf: DependenceDto, db: Session = Depends(table.execute)):
    #print(type_shelf)
    data = dict({COLUMN_DEPENDENCE: type_shelf})
    service = SaveDependenceService(db)
    return service.execute(data)