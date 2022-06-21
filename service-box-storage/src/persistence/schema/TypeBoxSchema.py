"""
    @name - TypeBoxSchema
    @description - Convertidor a diferentes tipos de type Box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.TypeBox import TypeBox
from src.model.response.TypeBoxResponse import TypeBoxResponse
from src.util.constant import COLUMN_TYPE_BOX_ID, COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF,COLUMN_TYPE_BOX_HEIGHT,COLUMN_TYPE_BOX_DEPTH,COLUMN_TYPE_BOX_WIDTH,COLUMN_TYPE_BOX_CREATION_DATE

class TypeBoxSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_TYPE_BOX_ID
        self.number_type_box = COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF
        self.depth = COLUMN_TYPE_BOX_DEPTH
        self.height = COLUMN_TYPE_BOX_HEIGHT
        self.width = COLUMN_TYPE_BOX_WIDTH
        self.creation_date = COLUMN_TYPE_BOX_CREATION_DATE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - TypeBox
    def entity(self, object) -> TypeBox:
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
    # @return - TypeBoxResponse
    def response(self, object) -> TypeBoxResponse:
        if object == None: 
            return object
        return TypeBoxResponse(
            id = object.id,
            number_type_box = object.number_type_box,
            depth = object.depth,
            height = object.height,
            width = object.width,
            date = object.date
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: object[self.id],
            self.number_type_box: object[self.number_type_box],
            self.depth: object[self.depth],
            self.height: object[self.height],
            self.width: object[self.width],
            self.creation_date: str(object[self.creation_date])
        }
        if id != None:
            data[self.creation_date]= create
        return data