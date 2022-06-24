"""
    @name - BlockSchema
    @description - Convertidor a diferentes tipos bloques
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.Block import Block
from src.model.response.BlockResponse import BlockResponse

from src.util.constant import DATABASE

class BlockSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['block']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.letter = self.table[1]
        self.flat = self.table[2]
        self.id_building = self.table[3]
        self.date = self.table[4]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Block
    def entity(self, object) -> Block:
        if object == None: 
            return object
        return object

    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - BlockResponse
    def response(self, object) -> BlockResponse:
        if object == None: 
            return object
        return BlockResponse(
            id = object.id,
            letter= object.letter,
            flat= object.flat,
            id_building= int(object.id_building),
            date= str(object.date),
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
            self.letter: object.letter, 
            self.flat: object.flat, 
            self.id_building: int(object.id_building),
            self.date: str(object.date),
        }
        if create != None:
            data[self.date]= str(create)
        return data