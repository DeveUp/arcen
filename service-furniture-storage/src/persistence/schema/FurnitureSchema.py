from src.model.response.FurnitureResponse import FurnitureResponse
from src.model.entity.Furniture import Furniture
from src.util.constant import COLUMN_FURNITURE_ID, COLUMN_FURNITURE_ID_BLOCK, COLUMN_FURNITURE_ID_TYPE_FURNITURE, COLUMN_FURNITURE_NUMBER_FURNITURE, COLUMN_FURNITURE_CREATION_DATE

class FurnitureSchema:

    def __init__(self):
        self.id = COLUMN_FURNITURE_ID
        self.id_block = COLUMN_FURNITURE_ID_BLOCK
        self.id_type_furniture = COLUMN_FURNITURE_ID_TYPE_FURNITURE
        self.number_furniture = COLUMN_FURNITURE_NUMBER_FURNITURE
        self.creation_date = COLUMN_FURNITURE_CREATION_DATE

    def entity(self, object) -> Furniture:
        if object == None: 
            return object
        return object
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> FurnitureResponse:
        if object == None: 
            return object
        return FurnitureResponse(
            id = object.id, 
            id_block = object.id_block, 
            id_type_furniture = object.id_type_furniture, 
            number_furniture = object.number_furniture,
            date= object.creation_date
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_FURNITURE_ID: object[self.id_block], 
            COLUMN_FURNITURE_ID_BLOCK: object[self.id_block], 
            COLUMN_FURNITURE_ID_TYPE_FURNITURE: object[self.id_type_furniture],  
            COLUMN_FURNITURE_NUMBER_FURNITURE: object[self.number_furniture],
            COLUMN_FURNITURE_CREATION_DATE: object[self.creation_date]
        }
        if create != None:
            data[self.creation_date]= create
        return data