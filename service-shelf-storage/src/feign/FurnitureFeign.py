from src.feign.Feign import Feign
from src.model.dto.FurnitureDto import FurnitureDto
from src.util.constant import FEIGN_ENDPOINT_FURNITURE, FEIGN_ENDPOINT_FURNITURE_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_FURNITURE_ERROR_SAVE

class FurnitureFeign:

    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_FURNITURE)
 
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_FURNITURE_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_FURNITURE_ERROR_SAVE)