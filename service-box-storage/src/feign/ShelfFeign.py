from src.feign.Feign import Feign
from src.model.dto.ShelfDto import ShelfDto
from src.util.constant import FEIGN_ENDPOINT_SHELF, FEIGN_ENDPOINT_SHELF_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_SHELF_ERROR_SAVE

class ShelfFeign:

    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_SHELF)
 
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_SHELF_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_SHELF_ERROR_SAVE)