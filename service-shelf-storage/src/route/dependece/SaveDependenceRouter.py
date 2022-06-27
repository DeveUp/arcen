"""
    @name - SaveDependenceRouter
    @description - Punto de entrada servicio dependence operacion registrar un dependence
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
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

# @Rest - Registra un dependence
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Dependence>
@router_save_dependence.post(endpoint, response_model = response, status_code=status ,tags=["Dependence"])
async def save(dependence: DependenceDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_DEPENDENCE: dependence})
    service = ServiceArcen(db)
    return service.execute(data)