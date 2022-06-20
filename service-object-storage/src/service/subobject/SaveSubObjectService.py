"""
    @name - SaveSubObjectService
    @description - Servicio para registrar un subobjeto
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

from src.persistence.repository.subobject.SaveSubObjectRepository import SaveSubObjectRepository
from src.persistence.schema.SubObjectSchema import SubObjectSchema

from src.util.constant import RESPONSE
from src.util.constant import FEIGN
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class SaveSubObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveSubObjectRepository(db)
        self.schema:SubObjectSchema = SubObjectSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['subobject']
        self.current_operation = FEIGN['type']['generic']['post']['save']

    # @override
    # @method - Registra un subobjeto
    # @parameter - data - Json con el subobjeto a registrar
    # @return - SubObject
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
                RESPONSE['subobject']['post']['save']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element