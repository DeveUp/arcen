from src.model.entity.Shelf import Shelf
from src.model.dto.ShelfDto import ShelfDto
from src.util.constant import COLUMN_SHELF_ID, COLUMN_SHELF_ID_DEPENDENCE, COLUMN_SHELF_ID_TYPE_SHELF, COLUMN_SHELF_ID_FURNITURE, COLUMN_SHELF_CREATION_DATE, COLUMN_SHELF_NUMBER_SHELF

class ShelfSchema:

    def __init__(self):
        self.id = COLUMN_SHELF_ID
        self.id_dependence = COLUMN_SHELF_ID_DEPENDENCE
        self.id_type_shelf = COLUMN_SHELF_ID_TYPE_SHELF
        self.id_furniture = COLUMN_SHELF_ID_FURNITURE
        self.number_shelf = COLUMN_SHELF_NUMBER_SHELF
        self.creation_date = COLUMN_SHELF_CREATION_DATE

    def shelf(self, shelf) -> Shelf:
        if shelf == None: 
            return shelf
        return shelf

    def shelf_other(self, shelf) -> Shelf:
        if shelf == None: 
            return shelf
        entity = Shelf(
            COLUMN_SHELF_ID = shelf[self.id],
            COLUMN_SHELF_ID_DEPENDENCE = shelf[self.id_dependence],
            COLUMN_SHELF_ID_TYPE_SHELF = shelf[self.id_type_shelf],
            COLUMN_SHELF_ID_FURNITURE = shelf[self.id_furniture],
            COLUMN_SHELF_NUMBER_SHELF = shelf[self.number_shelf],
            COLUMN_SHELF_CREATION_DATE = shelf[self.creation_date]
        )
        return entity
    
    def shelfs(self, shelfs) -> list:
        if shelfs == None: 
            return shelfs
        return [self.shelf(shelf) for shelf in shelfs]
    
    def shelf_dto(self, shelf) -> ShelfDto:
        if shelf == None: 
            return shelf
        return ShelfDto(
            COLUMN_SHELF_ID_DEPENDENCE = shelf[self.id_dependence],
            COLUMN_SHELF_ID_TYPE_SHELF = shelf[self.id_type_shelf],
            COLUMN_SHELF_ID_FURNITURE = shelf[self.id_furniture],
            COLUMN_SHELF_NUMBER_SHELF = shelf[self.number_shelf],
            COLUMN_SHELF_CREATION_DATE = shelf[self.creation_date]
        )

    def shelf_dict(self, shelf, create= None) -> dict:
        if shelf == None: 
            return shelf
        try:
            id = shelf[self.id]
        except:
            id = None
        try:
            creation_date = shelf[self.creation_date]
        except:
            creation_date = None
        data = {
            self.id_dependence: shelf[self.id_dependence],
            self.id_type_shelf: shelf[self.id_type_shelf],
            self.id_furniture: shelf[self.id_furniture],
            self.number_shelf: shelf[self.number_shelf]
        }
        if id != None:
            data[self.id]= id
        if creation_date != None:
            data[self.creation_date]= creation_date
        if create != None:
            data[self.creation_date]= create
        return data