"""
    @name - DependenceSchema
    @description - Convertidor a diferentes tipos de dependence
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
import imp
from src.model.entity.Dependence import Dependence
from src.model.response.DependenceResponse import DependenceResponse
from src.util.constant import COLUMN_DEPENDENCE_ID, COLUMN_DEPENDENCE_NAME, COLUMN_DEPENDENCE_CODE

class DependenceSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_DEPENDENCE_ID
        self.name = COLUMN_DEPENDENCE_NAME
        self.code = COLUMN_DEPENDENCE_CODE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Dependence
    def entity(self, object) -> Dependence:
        if object == None: 
            return object
        return object
        
    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def lists(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - DependenceResponse
    def response(self, object) -> DependenceResponse:
        if object == None: 
            return object
        return DependenceResponse(
            id = object.id,
            name = object.name,
            code = object.code
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        try:
            id = object[self.id]
        except:
            id = None
        data = {
            self.id: object[self.id],
            self.name: object[self.name],
            self.code: object[self.code]
        }
        if create != None:
            data[self.id]= id
        return data