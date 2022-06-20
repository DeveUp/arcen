"""
    @name - TypeObjectSchema
    @description - Convertidor a diferentes tipos de tipos de objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.TypeObject import TypeObject
from src.model.dto.TypeObjectDto import TypeObjectDto
from src.model.response.TypeObjectResponse import TypeObjectResponse

from src.util.constant import DATABASE

class TypeObjectSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['object']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.name:str = self.table[1]
        self.height:int = self.table[2]
        self.width:int = self.table[3]
        self.depth:int = self.table[4]
        self.date:str = self.table[5]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - TypeObject
    def entity(self, object) -> TypeObject:
        if object == None: 
            return object
        return object

    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - TypeObject  
    def response(self, object) -> TypeObjectResponse:
        if object == None: 
            return object
        entity = TypeObject(
            id = object.id,
            name = object.name,
            height = object.height,
            width = object.width,
            depth = object.depth,
            date = object.date
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
    def dto(self, object) -> TypeObjectDto:
        if object == None: 
            return object
        return TypeObjectDto(
            name = object.name,
            height = object.height,
            width = object.width,
            depth = object.depth
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
            self.name: object.name,
            self.height: object.height,
            self.width: object.width,
            self.depth: object.depth,
            self.date: str(object.date)
        }
        if create != None:
            data[self.date]= str(create)
        return data