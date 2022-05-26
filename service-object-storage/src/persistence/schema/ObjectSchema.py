from src.model.entity.Object import Object
from src.model.dto.ObjectDto import ObjectDto
from src.util.constant import COLUMN_OBJECT_ID, COLUMN_OBJECT_ID_TYPE_OBJECT,  COLUMN_OBJECT_ID_SUB_OBJECT, COLUMN_OBJECT_CREATION_DATE
from src.util.common import get_validate_field

class ObjectSchema:

    def __init__(self):
        self.id:int = COLUMN_OBJECT_ID
        self.id_type_object:int = COLUMN_OBJECT_ID_TYPE_OBJECT
        self.id_sub_object:int = COLUMN_OBJECT_ID_SUB_OBJECT
        self.creation_date:str = COLUMN_OBJECT_CREATION_DATE

    def entity(self, object) -> Object:
        if object == None: 
            return object
        return object
        
    def other(self, object) -> Object:
        if object == None: 
            return object
        entity = Object(
            COLUMN_OBJECT_ID = get_validate_field(object, self.id),
            COLUMN_OBJECT_ID_TYPE_OBJECT = get_validate_field(object, self.id_type_object),
            COLUMN_OBJECT_ID_SUB_OBJECT = get_validate_field(object, self.id_sub_object),
            COLUMN_OBJECT_CREATION_DATE = get_validate_field(object, self.creation_date),
        )
        return entity

    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.object(object) for object in objects]
    
    def dto(self, object) -> ObjectDto:
        if object == None: 
            return object
        return ObjectDto(
            COLUMN_OBJECT_ID_TYPE_OBJECT = get_validate_field(object, self.id_type_object),
            COLUMN_OBJECT_ID_SUB_OBJECT = get_validate_field(object, self.id_sub_object),
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_OBJECT_ID: get_validate_field(object, self.id),
            COLUMN_OBJECT_ID_TYPE_OBJECT: get_validate_field(object, self.id_type_object),
            COLUMN_OBJECT_ID_SUB_OBJECT: get_validate_field(object, self.id_sub_object),
            COLUMN_OBJECT_CREATION_DATE: get_validate_field(object, self.creation_date),
        }
        if create != None:
            data[self.creation_date]= create
        return data