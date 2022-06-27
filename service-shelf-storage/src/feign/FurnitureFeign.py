"""
    @name - ShelfFeign
    @description - Comunicacion con el microservicio Furniture servicio furniture.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.feign.Feign import Feign
from src.model.dto.FurnitureDto import FurnitureDto
from src.util.constant import FEIGN_ENDPOINT_FURNITURE, FEIGN_ENDPOINT_FURNITURE_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_FURNITURE_ERROR_SAVE

class FurnitureFeign:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_FURNITURE)
 
    # @method - Connsulta el microservicio furniture, al servicio furniture
    # @parameter - data - Json con el id de furniture a consultar
    # @return - Json
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_FURNITURE_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_FURNITURE_ERROR_SAVE)