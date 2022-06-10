from src.model.entity.TypeBox import TypeBox
from src.model.response.TypeBoxResponse import TypeBoxResponse
from src.util.constant import COLUMN_TYPE_BOX_ID, COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF,COLUMN_TYPE_BOX_HEIGHT,COLUMN_TYPE_BOX_DEPTH,COLUMN_TYPE_BOX_WIDTH,COLUMN_TYPE_BOX_CREATION_DATE

class TypeBoxSchema:

    def __init__(self):
        self.id = COLUMN_TYPE_BOX_ID
        self.number_type_box = COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF
        self.depth = COLUMN_TYPE_BOX_DEPTH
        self.height = COLUMN_TYPE_BOX_HEIGHT
        self.width = COLUMN_TYPE_BOX_WIDTH
        self.creation_date = COLUMN_TYPE_BOX_CREATION_DATE

    def entity(self, object) -> TypeBox:
        if object == None: 
            return object
        return object

    def lists(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> TypeBoxResponse:
        if object == None: 
            return object
        return TypeBoxResponse(
            COLUMN_TYPE_BOX_ID = object.id,
            COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF = object.number_type_box,
            COLUMN_TYPE_BOX_DEPTH = object.depth,
            COLUMN_TYPE_BOX_HEIGHT = object.height,
            COLUMN_TYPE_BOX_WIDTH = object.width,
            COLUMN_BOX_CREATION_DATE = object.date
        )

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