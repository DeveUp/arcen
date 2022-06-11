from src.service.IService import IService

from src.persistence.repository.document_version.FindByIdDocumentVersionRepository import FindByIdDocumentVersionRepository
from src.persistence.schema.DocumentVersionSchema import DocumentVersionSchema

from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_VERSION_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdDocumentVersionService(IService):

    def __init__(self):
        self.repository = FindByIdDocumentVersionRepository()
        self.schema = DocumentVersionSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_VERSION_FIND_BY_ID_NOT_CONTENT)
        return element