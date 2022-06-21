"""
    @name - TypeFurnitureSchema
    @description - Convertidor a diferentes tipos de tipos de tipo de muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.TypeFurniture import TypeFurniture
from src.model.response.TypeFurnitureResponse import TypeFurnitureResponse

from src.util.constant import DATABASE

class TypeFurnitureSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['type_furniture']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.number_type_furniture = self.table[1]
        self.count_rack = self.table[2]
        self.count_row = self.table[3]
        self.depth = self.table[4]
        self.height = self.table[5]
        self.width = self.table[6]
        self.date = self.table[7]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - TypeFurniture
    def entity(self, object) -> TypeFurniture:
        if object == None: 
            return object
        return object

    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - TypeFurnitureResponse
    def response(self, object) -> TypeFurnitureResponse:
        if object == None: 
            return object
        return TypeFurnitureResponse(
            id = object.id,
            number_type_furniture= object.number_type_furniture,
            count_rack= object.count_rack,
            count_row= object.count_row,
            depth= object.depth,
            height= object.height,
            width= object.width,
            date= str(object.date)
        )
    
    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]


    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: object.id,
            self.number_type_furniture: object.number_type_furniture,
            self.count_rack: object.count_rack,  
            self.count_row: object.count_row,
            self.depth: object.depth,
            self.height:object.height,
            self.width: object.width,
            self.date: str(object.date)
        }
        if create != None:
            data[self.date]= str(create)
        return data