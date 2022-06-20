from src.feign.Feign import Feign
from src.model.dto.DependenceDto import DependenceDto
from src.util.constant import FEIGN_ENDPOINT_DEPENDENCE, FEIGN_ENDPOINT_DEPENDENCE_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT

class DependenceFeign:

    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_DEPENDENCE)
 
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_DEPENDENCE_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)