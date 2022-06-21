"""
    @name - UpdateFurnitureService
    @description - Servicio para actualizar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign

from src.service.IService import IService
from src.service.block.FindByIdBlockService import FindByIdBlockRepository

from src.persistence.repository.furniture.UpdateFurnitureRepository import UpdateFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

from src.util.constant import RESPONSE
from src.util.constant import DATABASE
from src.util.constant import FEIGN
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error


class UpdateFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = UpdateFurnitureRepository(db)
        self.find_by_id_block = FindByIdBlockRepository(db)
        self.schema = FurnitureSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['furniture']
        self.current_operation = FEIGN['type']['generic']['put']['update']

    # @override
    # @method - Actualizar un mueble por su pk
    # @parameter - data - Json con el mueble a actualizar
    # @return - Furniture
    def execute(self, data:dict):
        # Consulta que exista un bloque con ese pk
        self.find_by_id_block.execute(dict({
            DATABASE['table']['block']['pk']: str(data[DATABASE['table']['furniture']['name']].id_block)
        }))
        # Se registra el mueble
       # Se registra el mueble
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except HTTPException as error_http:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                feign_audit_build_error(error_http.status_code, error_http.detail)
            )
        except:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                RESPONSE['funiture']['put']['update']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element