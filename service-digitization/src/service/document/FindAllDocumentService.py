"""
    @description - Servicio documento operacion consultar todos los documentos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.service.IService import IService

from src.persistence.repository.document.FindAllDocumentRepository import FindAllDocumentRepository
from src.persistence.schema.DocumentSchema import DocumentSchema

class FindAllDocumentService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindAllDocumentRepository()
        self.schema = DocumentSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)