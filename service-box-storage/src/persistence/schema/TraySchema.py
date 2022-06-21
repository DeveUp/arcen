"""
    @name - TraySchema
    @description - Convertidor a diferentes tipos de tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.Tray import Tray
from src.model.response.TrayResponse import TrayResponse
from src.util.constant import  COLUMN_TRAY_ID,COLUMN_TRAY_ID_SHELF,COLUMN_TRAY_DEPTH,COLUMN_TRAY_HEIGHT,COLUMN_TRAY_WIDTH,COLUMN_TRAY_CREATION_DATE

class TraySchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.id = COLUMN_TRAY_ID
        self.id_shelf = COLUMN_TRAY_ID_SHELF
        self.depth = COLUMN_TRAY_DEPTH
        self.height = COLUMN_TRAY_HEIGHT
        self.width = COLUMN_TRAY_WIDTH
        self.creation_date = COLUMN_TRAY_CREATION_DATE

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Tray
    def entity(self, object) -> Tray:
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
    # @return - TrayResponse
    def response(self, object) -> TrayResponse:
        if object == None: 
            return object
        return TrayResponse(
            id = object.id,
            id_shelf = object.id_shelf,
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
        data = {
            self.id: object[self.id],
            self.id_shelf: object[self.id_shelf],
            self.depth: object[self.depth],
            self.height: object[self.height],
            self.width: object[self.width],
            self.creation_date: str(object[self.creation_date])
        }
        if id != None:
            data[self.creation_date]= create
        return data