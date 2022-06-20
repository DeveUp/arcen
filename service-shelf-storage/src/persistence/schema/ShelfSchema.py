from src.model.entity.Shelf import Shelf
from src.model.response.ShelfResponse import ShelfResponse
from src.util.constant import COLUMN_SHELF_ID, COLUMN_SHELF_ID_DEPENDENCE, COLUMN_SHELF_ID_TYPE_SHELF, COLUMN_SHELF_ID_FURNITURE, COLUMN_SHELF_CREATION_DATE, COLUMN_SHELF_NUMBER_SHELF

class ShelfSchema:

    def __init__(self):
        self.id = COLUMN_SHELF_ID
        self.id_dependence = COLUMN_SHELF_ID_DEPENDENCE
        self.id_type_shelf = COLUMN_SHELF_ID_TYPE_SHELF
        self.id_furniture = COLUMN_SHELF_ID_FURNITURE
        self.number_shelf = COLUMN_SHELF_NUMBER_SHELF
        self.creation_date = COLUMN_SHELF_CREATION_DATE

    def entity(self, object) -> Shelf:
        if object == None: 
            return object
        return object

    def lists(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> ShelfResponse:
        if object == None: 
            return object
        return ShelfResponse(
            id = object.id,
            id_dependence = object.id_dependence,
            id_type_shelf = object.id_type_shelf,
            id_furniture = object.id_furniture,
            number_shelf = object.number_shelf,
            date =str( object.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: object[self.id],
            self.id_dependence: object[self.id_dependence],
            self.id_type_shelf: object[self.id_type_shelf],
            self.id_furniture: object[self.id_furniture],
            self.number_shelf: object[self.number_shelf],
            self.creation_date: str(object[self.creation_date])
        }
        if id != None:
            data[self.creation_date]= create
        return data