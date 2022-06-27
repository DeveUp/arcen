"""
    @name - ShelfSchema
    @description - Convertidor a diferentes tipos de shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.TypeShelf import TypeShelf
from src.model.dto.TypeShelfDto import TypeShelfDto
from src.model.response.TypeShelfResponse import TypeShelfResponse
from src.util.constant import COLUMN_TYPE_SHELF_ID, COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF, COLUMN_TYPE_SHELF_DEPTH, COLUMN_TYPE_SHELF_HEIGHT, COLUMN_TYPE_SHELF_WIDTH, COLUMN_TYPE_SHELF_CREATION_DATE

class TypeShelfSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_TYPE_SHELF_ID
        self.number_type_shelf = COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF
        self.depth = COLUMN_TYPE_SHELF_DEPTH
        self.height = COLUMN_TYPE_SHELF_HEIGHT
        self.width = COLUMN_TYPE_SHELF_WIDTH
        self.creation_date = COLUMN_TYPE_SHELF_CREATION_DATE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - TypeShelf
    def entity(self, object) -> TypeShelf:
        #print(type_shelf)
        if object == None: 
            return object
        return object
    
    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def lists(self, type_shelfs) -> list:
        if type_shelfs == None: 
            return type_shelfs
        return [self.type_shelf(type_shelf) for type_shelf in type_shelfs]
    
    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - TypeShelfResponse
    def response(self, object) -> TypeShelfResponse:
        if object == None: 
            return object
        return TypeShelfResponse(
            id = object.id,
            number_type_shelf = object.number_type_shelf,
            depth = object.depth,
            height = object.height,
            width = object.width,
            date = str(object.date)
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
            self.number_type_shelf: object[self.number_type_shelf],
            self.depth: object[self.depth],
            self.height: object[self.height],
            self.width: object[self.width],
            self.date : object[self.date]
        }
        if create != None:
            data[self.creation_date]= create
        return data