"""
    @name - FurnitureSchema
    @description - Convertidor a diferentes tipos muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.response.FurnitureResponse import FurnitureResponse
from src.model.entity.Furniture import Furniture

from src.util.constant import DATABASE

class FurnitureSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['furniture']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.id_block = self.table[1]
        self.id_type_furniture = self.table[2]
        self.number_furniture = self.table[3]
        self.date = self.table[4]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Furniture
    def entity(self, object) -> Furniture:
        if object == None: 
            return object
        return object

    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - FurnitureResponse
    def response(self, object) -> FurnitureResponse:
        if object == None: 
            return object  
        return FurnitureResponse(
            id = object.id, 
            id_block = object.id_block, 
            id_type_furniture = object.id_type_furniture, 
            number_furniture = object.number_furniture,
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
            self.id: object[self.id_block], 
            self.id_block: object[self.id_block], 
            self.id_type_furniture: object[self.id_type_furniture],  
            self.number_furniture: object[self.number_furniture],
            self.date: str(object[self.date])
        }
        if create != None:
            data[self.date]= str(create)
        return data