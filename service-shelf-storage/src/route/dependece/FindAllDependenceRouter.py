from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.dependence.FindAllDependenceService import FindAllDependenceService
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_DEPENDENCE, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_dependence = APIRouter()
table = TableArcen()

status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_dependence.get(ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_FIND_ALL,status_code=status)
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllDependenceService(db)
    return service.execute(dict())