"""
    @name - UpdateShelfRouter
    @description - Punto de entrada servicio type shelf operacion actualizar un type shelf por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeShelfDto import TypeShelfDto
from src.model.response.TypeShelfResponse import TypeShelfResponse as ResponseArcen
from src.service.type_shelf.UpdateTypeShelfService import UpdateTypeShelfService as ServiceArcen
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF, COLUMN_TYPE_SHELF_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_UPDATE

router_update_type_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

# @Rest - Actualiza un type shelf por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeShelf>
@router_update_type_shelf.put(endpoint ,response_model = response ,status_code=status,tags=["TypeShelf"])
async def update(id: str, type_shelf: TypeShelfDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_TYPE_SHELF_ID: id, 
        COLUMN_TYPE_SHELF: type_shelf
    })
    service = ServiceArcen(db)
    return service.execute(data)