from src.model.entity.TypeObject import TypeObject
from src.model.dto.TypeObjectDto import TypeObjectDto
from src.util.constant import COLUMN_TYPE_OBJECT_ID, COLUMN_TYPE_OBJECT_NAME, COLUMN_TYPE_OBJECT_HEIGHT, COLUMN_TYPE_OBJECT_WIDTH, COLUMN_TYPE_OBJECT_DEPTH, COLUMN_TYPE_OBJECT_CREATION_DATE
from src.util.common import get_validate_field

class TypeObjectSchema:

    def __init__(self):
        self.id:int = COLUMN_TYPE_OBJECT_ID
        self.name:str = COLUMN_TYPE_OBJECT_NAME
        self.height:int = COLUMN_TYPE_OBJECT_HEIGHT
        self.width:int = COLUMN_TYPE_OBJECT_WIDTH
        self.depth:int = COLUMN_TYPE_OBJECT_DEPTH
        self.creation_date:str = COLUMN_TYPE_OBJECT_CREATION_DATE

    def entity(self, object) -> TypeObject:
        if object == None: 
            return object
        return object
        
    def other(self, object) -> TypeObject:
        if object == None: 
            return object
        entity = TypeObject(
            COLUMN_TYPE_OBJECT_ID = get_validate_field(object, self.id),
            COLUMN_TYPE_OBJECT_NAME = get_validate_field(object, self.name),
            COLUMN_TYPE_OBJECT_HEIGHT = get_validate_field(object, self.height),
            COLUMN_TYPE_OBJECT_WIDTH = get_validate_field(object, self.width),
            COLUMN_TYPE_OBJECT_DEPTH = get_validate_field(object, self.depth),
            COLUMN_TYPE_OBJECT_CREATION_DATE = get_validate_field(object, self.creation_date)
        )
        return entity

    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def dto(self, object) -> TypeObjectDto:
        if object == None: 
            return object
        return TypeObjectDto(
            COLUMN_TYPE_OBJECT_NAME = get_validate_field(object, self.name),
            COLUMN_TYPE_OBJECT_HEIGHT = get_validate_field(object, self.height),
            COLUMN_TYPE_OBJECT_WIDTH = get_validate_field(object, self.width),
            COLUMN_TYPE_OBJECT_DEPTH = get_validate_field(object, self.depth)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_TYPE_OBJECT_ID: get_validate_field(object, self.id),
            COLUMN_TYPE_OBJECT_NAME: get_validate_field(object, self.name),
            COLUMN_TYPE_OBJECT_HEIGHT: get_validate_field(object, self.height),
            COLUMN_TYPE_OBJECT_WIDTH: get_validate_field(object, self.width),
            COLUMN_TYPE_OBJECT_DEPTH: get_validate_field(object, self.depth),
            COLUMN_TYPE_OBJECT_CREATION_DATE: get_validate_field(object, self.creation_date)
        }
        if create != None:
            data[self.creation_date]= create
        return data