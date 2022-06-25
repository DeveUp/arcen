"""
    @name - DependenceFeign
    @description - Comunicacion con el microservicio Shelf servicio dependence.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.feign.Feign import Feign
from src.model.dto.DependenceDto import DependenceDto
from src.util.constant import FEIGN_ENDPOINT_DEPENDENCE, FEIGN_ENDPOINT_DEPENDENCE_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT

class DependenceFeign:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_DEPENDENCE)
 
    # @method - Connsulta el microservicio shelf, al servicio dependence
    # @parameter - data - Json con el id de dependence a consultar
    # @return - Json
    def findByID(self, data):
        return self.feign.get(FEIGN_ENDPOINT_DEPENDENCE_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)