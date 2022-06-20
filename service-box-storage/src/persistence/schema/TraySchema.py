from src.model.entity.Tray import Tray
from src.model.response.TrayResponse import TrayResponse
from src.util.constant import  COLUMN_TRAY_ID,COLUMN_TRAY_ID_SHELF,COLUMN_TRAY_DEPTH,COLUMN_TRAY_HEIGHT,COLUMN_TRAY_WIDTH,COLUMN_TRAY_CREATION_DATE

class TraySchema:

    def __init__(self):
        self.id = COLUMN_TRAY_ID
        self.id_shelf = COLUMN_TRAY_ID_SHELF
        self.depth = COLUMN_TRAY_DEPTH
        self.height = COLUMN_TRAY_HEIGHT
        self.width = COLUMN_TRAY_WIDTH
        self.creation_date = COLUMN_TRAY_CREATION_DATE

    def entity(self, object) -> Tray:
        if object == None: 
            return object
        return object

    def lists(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
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