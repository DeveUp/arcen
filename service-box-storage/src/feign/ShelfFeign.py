"""
    @name - ShelfFeign
    @description - Comunicacion con el microservicio Shelf servicio shelf.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.feign.Feign import Feign
from src.model.dto.ShelfDto import ShelfDto
from src.util.constant import FEIGN_ENDPOINT_SHELF, FEIGN_ENDPOINT_SHELF_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_SHELF_ERROR_SAVE

class ShelfFeign:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_SHELF)
 
    # @method - Connsulta el microservicio shelf, al servicio shelf
    # @parameter - data - Json con el id de shelf a consultar
    # @return - Json
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_SHELF_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_SHELF_ERROR_SAVE)