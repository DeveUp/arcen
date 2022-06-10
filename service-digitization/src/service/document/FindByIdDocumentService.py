from src.service.IService import IService
from src.persistence.repository.document.FindByIdDocumentRepository import FindByIdDocumentRepository
from src.persistence.schema.DocumentSchema import DocumentSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdDocumentService(IService):

    def __init__(self):
        self.repository = FindByIdDocumentRepository()
        self.schema = DocumentSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            return self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_FIND_BY_ID_NOT_CONTENT)