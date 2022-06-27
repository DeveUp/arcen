"""
    @name - UpdateTrayRouter
    @description - Punto de entrada servicio tray operacion actualizar un tray por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TrayDto import TrayDto
from src.model.response.TrayResponse import TrayResponse as ResponseArcen
from src.service.tray.UpdateTrayService import UpdateTrayService as ServiceArcen
from src.persistence.database.table.TrayTable import TrayTable as TableArcen
from src.util.constant import COLUMN_TRAY, COLUMN_TRAY_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_TRAY, ENDPOINT_GENERIC_UPDATE

router_update_tray = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TRAY+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

# @Rest - Actualiza un tray por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Tray>
@router_update_tray.put(endpoint ,response_model = response ,status_code=status,tags=["Tray"])
async def update(id: str, tray: TrayDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TRAY_ID: id, 
        COLUMN_TRAY: tray
    })
    service = ServiceArcen(db)
    return service.execute(data)