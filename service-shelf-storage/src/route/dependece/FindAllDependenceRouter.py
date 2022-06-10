from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.dependence.FindAllDependenceService import FindAllDependenceService as FindAllService
from src.persistence.database.table.DependenceTable import DependenceTable as TableArcen
from src.util.constant import ENDPOINT_APP,RESPONSE_MODEL_DEPENDENCE_FIND_ALL, ENDPOINT_APP_DEPENDENCE, ENDPOINT_GENERIC_FIND_ALL,RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_dependence = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_DEPENDENCE+ENDPOINT_GENERIC_FIND_ALL
response=RESPONSE_MODEL_DEPENDENCE_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_dependence.get(endpoint,status_code=status,tags=["Dependence"])
async def find_all(db: Session = Depends(table.execute)):
    service = FindAllService(db)
    return service.execute(dict())