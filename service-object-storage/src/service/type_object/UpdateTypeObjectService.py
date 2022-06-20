"""
    @name - UpdateTypeObjectService
    @description - Servicio para actualizar un tipo de objeto por su pk
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

from src.persistence.repository.type_object.UpdateTypeObjectRepository import UpdateTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

from src.util.constant import RESPONSE
from src.util.constant import FEIGN
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class UpdateTypeObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = UpdateTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['type_object']
        self.current_operation = FEIGN['type']['generic']['put']['update']

    # @override
    # @method - Actualizar un tipo de objeto por su pk
    # @parameter - data - Json con el tipo de objeto a actualizar
    # @return - TypeObject
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
                RESPONSE['type_object']['put']['update']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element