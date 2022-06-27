"""
    @name - UpdateShelfRouter
    @description - Punto de entrada servicio shelf operacion actualizar un shelf por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.ShelfDto import ShelfDto
from src.model.response.ShelfResponse import ShelfResponse as ResponseArcen
from src.service.shelf.UpdateShelfService import UpdateShelfService as ServiceArcen
from src.persistence.database.table.ShelfTable import ShelfTable as TableArcen
from src.util.constant import COLUMN_SHELF, COLUMN_SHELF_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP_SHELF, ENDPOINT_GENERIC_UPDATE

router_update_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_SHELF+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

# @Rest - Actualiza un shelf por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Shelf>
@router_update_shelf.put(endpoint,response_model = response,status_code=status,tags=["Shelf"])
async def update(id: str, shelf: ShelfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_SHELF_ID: id, 
        COLUMN_SHELF: shelf
    })
    service = ServiceArcen(db)
    return service.execute(data)