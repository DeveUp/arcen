"""
    @description - Servicio documento operacion registrar documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException

from src.feign.AuditFeign import AuditFeign

from src.service.IService import IService
from src.service.document.FindByIdDocumentService import FindByIdDocumentService

from src.persistence.repository.document.SaveDocumentRepository import SaveDocumentRepository
from src.persistence.schema.DocumentSchema import DocumentSchema

from src.util.constant import DATABASE
from src.util.constant import RESPONSE
from src.util.common import generate_date
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class SaveDocumentService(IService):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.repository = SaveDocumentRepository()
        self.find_by_id_document = FindByIdDocumentService()
        self.schema = DocumentSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = "DOCUMENTO"
        self.current_operation = "RESGISTRAR"

    # @override
    # @method - Registra una documento
    # @parameter - data - Json con el documento
    # @return - Document
    def execute(self, data:dict):
        try:
            self.data = DATABASE['table']['document']['name']
            document = self.schema.dict(dict(data[self.data]), generate_date())
            data = dict({self.data: self.schema.request(dict(document))})
            element = self.repository.execute(data)
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
                RESPONSE['document']['post']['save']['error']['default']
            )
        # Se consulta el documento registrado
        print(element)
        element = self.find_by_id(str(element))
        print("Se consulto")
        print(element)
        # Se registra la auditoria
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        print("Se Registro la auditoria")
        return element

    # @method - Consulta un documento por su pk
    # @parameter - id - Representa el pk del documento
    # @return - Document
    def find_by_id(self, id):
        self.data = DATABASE['table']['document']
        data = dict({self.data['column'][0]: id})
        return self.find_by_id_document.execute(data)