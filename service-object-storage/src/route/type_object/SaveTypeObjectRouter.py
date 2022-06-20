"""
    @name - SaveTypeObjectRouter
    @description - Punto de entrada servicio tipo de objeto operacion registrar un tipo de objeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeObjectDto import TypeObjectDto as DtoArcen
from src.model.response.TypeObjectResponse import TypeObjectResponse as ResponseArcen

from src.service.type_object.SaveTypeObjectService import SaveTypeObjectService as ServiceArcen
from src.persistence.database.table.TypeObjectTable import TypeObjectTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import RESPONSE
from src.util.constant import DATABASE

router_save_type_object = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_object']['path']+ENDPOINT['operation']['post']['save']
status = RESPONSE['type_object']['post']['save']['success']['default']['code']
response = ResponseArcen
info_data = DATABASE['table']['type_object']['name']

# @Rest - Registra un tipo de objeto
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<TypeObject>
@router_save_type_object.post(endpoint, response_model = response, status_code= status)
async def save(block: DtoArcen, db: Session = Depends(table.execute)):
    data = dict({
        info_data: block
    })
    service = ServiceArcen(db)
    return service.execute(data)