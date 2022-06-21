"""
    @name - SaveTypeFurnitureService
    @description - Servicio para registrar un tipo de mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.feign.AuditFeign import AuditFeign

from src.persistence.repository.type_furniture.SaveTypeFurnitureRepository import SaveTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

from src.util.constant import RESPONSE
from src.util.constant import DATABASE
from src.util.constant import FEIGN
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class SaveTypeFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['type_furniture']
        self.current_operation = FEIGN['type']['generic']['post']['save']

    # @override
    # @method - Registra un tipo de mueble
    # @parameter - data - Json con el tipo de mueble a registrar
    # @return - TypeFurniture
    def execute(self, data:dict):
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
                RESPONSE['type_funiture']['post']['save']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element