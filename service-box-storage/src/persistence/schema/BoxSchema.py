"""
    @name - BoxSchema
    @description - Convertidor a diferentes tipos de box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.Box import Box
from src.model.response.BoxResponse import BoxResponse
from src.util.constant import COLUMN_BOX_ID, COLUMN_BOX_ID_TRAY, COLUMN_BOX_ID_TYPE_BOX, COLUMN_BOX_NUMBER_BOX,COLUMN_BOX_CREATION_DATE

class BoxSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_BOX_ID
        self.id_tray = COLUMN_BOX_ID_TRAY
        self.id_type_box = COLUMN_BOX_ID_TYPE_BOX
        self.number_box = COLUMN_BOX_NUMBER_BOX
        self.creation_date = COLUMN_BOX_CREATION_DATE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Box
    def entity(self, object) -> Box:
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
    # @return - BoxResponse
    def response(self, object) -> BoxResponse:
        if object == None: 
            return object
        return BoxResponse(
            id = object.id,
            id_tray = object.id_tray,
            id_type_box = object.id_type_box,
            number_box = object.number_box,
            date = str(object.date)
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
            self.id_tray: object[self.id_tray],
            self.id_type_box: object[self.id_type_box],
            self.number_box: object[self.number_box],
            self.creation_date: str(object[self.creation_date])
        }
        if id != None:
            data[self.creation_date]= create
        return data