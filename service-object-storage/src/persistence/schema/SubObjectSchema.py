"""
    @name - SubObjectSchema
    @description - Convertidor a diferentes tipos subobjecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.SubObject import SubObject
from src.model.dto.SubObjectDto import SubObjectDto
from src.model.response.SubObjectResponse import SubObjectResponse

from src.util.constant import DATABASE

class SubObjectSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['object']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.box:str = self.table[1]
        self.number:int = self.table[2]
        self.date:str = self.table[3]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - SubObject
    def entity(self, object) -> SubObject:
        if object == None: 
            return object
        return object
        
    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - SubObjectResponse
    def response(self, object) -> SubObjectResponse:
        if object == None: 
            return object
        entity = SubObjectResponse(
            id = object.id,
            box = object.box,
            number = object.number,
            date = str(object.date)
        )
        return entity

    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @method - Convierte un objeto a un dto
    # @parameter - object - Representa los objecto a convertir
    # @return - SubObjectDto
    def dto(self, object) -> SubObjectDto:
        if object == None: 
            return object
        return SubObjectDto(
            box = object.box,
            number = object.number
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: object.id,
            self.box: object.box,
            self.number: object.number,
            self.date: str(object.date)
        }
        if create != None:
            data[self.date]= str(create)
        return data