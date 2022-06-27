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
from src.util.common_digitization import create_path_image, create_folder, encode, convert_images_to_pdf

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
            self.table = DATABASE['table']['document']
            self.data = dict(data[self.table['name']])
            # Se construye la peticion
            document = self.schema.dict(self.data, generate_date())
            # Procesa los documentos
            self.documents(
                self.data[self.table['column'][1]], 
                self.data[DATABASE['table']['document_location']['column'][1]],
            )
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
        return None

    # @method - Consulta un documento por su pk
    # @parameter - id - Representa el pk del documento
    # @return - Document
    def find_by_id(self, id):
        self.data = DATABASE['table']['document']
        data = dict({self.data['column'][0]: id})
        return self.find_by_id_document.execute(data)
    
    # @method - Convierte el base64 en una imagen y la guarda en una carpeta temporal
    # @parameter - data - Represeta una lista con los documentos escaneados
    # @return - list
    def documents(self, data:list, filename):
        path_documents = []
        path = create_path_image()
        is_dir = create_folder(path)
        for document in data:
            base64 = document['base64']
            file_name = document['file_name']
            path_image = encode(base64, path, file_name)
            print(path)
            print(is_dir)
            print(path_image)
        convert_images_to_pdf(path, filename)
        return path_documents