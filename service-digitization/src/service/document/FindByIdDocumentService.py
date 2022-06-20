"""
    @description - Servicio documento operacion consultar por el pk del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.service.IService import IService

from src.persistence.repository.document.FindByIdDocumentRepository import FindByIdDocumentRepository
from src.persistence.schema.DocumentSchema import DocumentSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdDocumentService(IService):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.repository = FindByIdDocumentRepository()
        self.schema = DocumentSchema()

    # @override
    # @method - Consulta un documento por el pk
    # @parameter - data - Json con el pk del documento
    # @return - Document
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_exception_http(RESPONSE['document']['get']['find_by_id']['error']['default'])
        return element