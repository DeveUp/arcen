"""
    @name - RoleSchema
    @description - Convertidor a diferentes tipos de role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.Role import Role
from src.model.response.RoleResponse import RoleResponse
from src.util.constant import COLUMN_ROLE_ID, COLUMN_ROLE_NAME, COLUMN_ROLE_DATE

class RoleSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_ROLE_ID
        self.id_name = COLUMN_ROLE_NAME
        self.creation_date = COLUMN_ROLE_DATE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Role
    def entity(self, object) -> Role:
        if object == None: 
            return object
        return object
    
    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - RoleResponse
    def response(self, object) -> RoleResponse:
        if object == None: 
            return object
        return RoleResponse(
            id = object.id, 
            name = object.name, 
            date = str(object.date),
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_ROLE_ID: object[self.id], 
            COLUMN_ROLE_NAME: object[self.name],
            COLUMN_ROLE_DATE: object[self.date]
        }
        if create != None:
            data[self.creation_date]= create
        return data