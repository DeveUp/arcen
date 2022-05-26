from src.model.entity.SubObject import SubObject
from src.model.dto.SubObjectDto import SubObjectDto
from src.util.constant import COLUMN_SUB_OBJECT_ID, COLUMN_SUB_OBJECT_BOX, COLUMN_SUB_OBJECT_NUMBER, COLUMN_SUB_OBJECT_CREATION_DATE
from src.util.common import get_validate_field

class SubObjectSchema:

    def __init__(self):
        self.id:int = COLUMN_SUB_OBJECT_ID
        self.box:str = COLUMN_SUB_OBJECT_BOX
        self.number:int = COLUMN_SUB_OBJECT_NUMBER
        self.creation_date:str = COLUMN_SUB_OBJECT_CREATION_DATE

    def entity(self, object) -> SubObject:
        if object == None: 
            return object
        return object
        
    def other(self, object) -> SubObject:
        if object == None: 
            return object
        entity = SubObject(
            COLUMN_SUB_OBJECT_ID = get_validate_field(object, self.id),
            COLUMN_SUB_OBJECT_BOX = get_validate_field(object, self.box),
            COLUMN_SUB_OBJECT_NUMBER = get_validate_field(object, self.number),
            COLUMN_SUB_OBJECT_CREATION_DATE = get_validate_field(object, self.creation_date)
        )
        return entity

    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def dto(self, object) -> SubObjectDto:
        if object == None: 
            return object
        return SubObjectDto(
            COLUMN_SUB_OBJECT_BOX = get_validate_field(object, self.box),
            COLUMN_SUB_OBJECT_NUMBER = get_validate_field(object, self.number)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_SUB_OBJECT_ID: get_validate_field(object, self.id),
            COLUMN_SUB_OBJECT_BOX: get_validate_field(object, self.box),
            COLUMN_SUB_OBJECT_NUMBER: get_validate_field(object, self.number),
            COLUMN_SUB_OBJECT_CREATION_DATE: get_validate_field(object, self.creation_date)
        }
        if create != None:
            data[self.creation_date]= create
        return data