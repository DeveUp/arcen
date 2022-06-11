from src.service.IService import IService
from src.persistence.repository.document_location.FindByIdDocumentLocationRepository import FindByIdDocumentLocationRepository
from src.persistence.schema.DocumentLocationSchema import DocumentLocationSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_LOCATION_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdDocumentLocationService(IService):

    def __init__(self):
        self.repository = FindByIdDocumentLocationRepository()
        self.schema = DocumentLocationSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DOCUMENT_LOCATION_FIND_BY_ID_NOT_CONTENT)
        return element