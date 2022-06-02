from src.model.entity.TypeFurniture import TypeFurniture
from src.model.response.TypeFurnitureResponse import TypeFurnitureResponse
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_COUNT_RACK, COLUMN_TYPE_FURNITURE_COUNT_ROW, COLUMN_TYPE_FURNITURE_DEPTH, COLUMN_TYPE_FURNITURE_HEIGHT, COLUMN_TYPE_FURNITURE_WIDTH, COLUMN_TYPE_FURNITURE_CREATION_DATE

class TypeFurnitureSchema:

    def __init__(self):
        self.id = COLUMN_TYPE_FURNITURE_ID
        self.number_type_furniture = COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE
        self.count_rack = COLUMN_TYPE_FURNITURE_COUNT_RACK
        self.count_row = COLUMN_TYPE_FURNITURE_COUNT_ROW
        self.depth = COLUMN_TYPE_FURNITURE_DEPTH
        self.height = COLUMN_TYPE_FURNITURE_HEIGHT
        self.width = COLUMN_TYPE_FURNITURE_WIDTH
        self.creation_date = COLUMN_TYPE_FURNITURE_CREATION_DATE

    def entity(self, object) -> TypeFurniture:
        if object == None: 
            return object
        return object
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
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
            date= object.creation_date
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_TYPE_FURNITURE_ID: object.id,
            COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE: object.number_type_furniture,
            COLUMN_TYPE_FURNITURE_COUNT_RACK: object.count_rack,  
            COLUMN_TYPE_FURNITURE_COUNT_ROW: object.count_row,
            COLUMN_TYPE_FURNITURE_DEPTH: object.depth,
            COLUMN_TYPE_FURNITURE_HEIGHT:object.height,
            COLUMN_TYPE_FURNITURE_WIDTH: object.width,
            COLUMN_TYPE_FURNITURE_CREATION_DATE: object.creation_date
        }
        if create != None:
            data[self.creation_date]= create
        return data