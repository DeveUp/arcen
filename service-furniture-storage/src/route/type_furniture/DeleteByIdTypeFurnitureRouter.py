"""
    @name - DeleteByIdTypeFurnitureRouter
    @description - Punto de entrada servicio tipo de mueble operacion eliminar tipo de mueble por el pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.service.type_furniture.DeleteByIdTypeFurnitureService import DeleteByIdTypeFurnitureService as ServiceArcen

from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen

from src.util.constant import ENDPOINT
from src.util.constant import DATABASE
from src.util.constant import RESPONSE

router_detele_by_id_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT['path']+ENDPOINT['service']['type_furniture']['path']+ENDPOINT['operation']['delete']['delete_by_id']
status = RESPONSE['type_furniture']['delete']['delete_by_id']['success']['default']['code']
info_data = DATABASE['table']['type_furniture']['column'][0]

# @Rest - Elimina un tipo de mueble por su pk
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<Void>
@router_detele_by_id_type_furniture.delete(endpoint, status_code= status)
async def delete_by_id(id:str, db:Session= Depends(table.execute)):
    data = dict({
        info_data:id
    })
    service = ServiceArcen(db)
    service.execute(data)