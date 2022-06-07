from src.model.entity.TypeShelf import TypeShelf
from src.model.dto.TypeShelfDto import TypeShelfDto
from src.util.constant import COLUMN_TYPE_SHELF_ID, COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF, COLUMN_TYPE_SHELF_DEPTH, COLUMN_TYPE_SHELF_HEIGHT, COLUMN_TYPE_SHELF_WIDTH, COLUMN_TYPE_SHELF_CREATION_DATE

class TypeShelfSchema:

    def __init__(self):
        self.id = COLUMN_TYPE_SHELF_ID
        self.number_type_shelf = COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF
        self.depth = COLUMN_TYPE_SHELF_DEPTH
        self.height = COLUMN_TYPE_SHELF_HEIGHT
        self.width = COLUMN_TYPE_SHELF_WIDTH
        self.creation_date = COLUMN_TYPE_SHELF_CREATION_DATE

    def type_shelf(self, type_shelf) -> TypeShelf:
        #print(type_shelf)
        if type_shelf == None: 
            return type_shelf
        return type_shelf

    def type_shelf_other(self, type_shelf) -> TypeShelf:
        if type_shelf == None: 
            return type_shelf
        entity = TypeShelf(
            COLUMN_TYPE_SHELF_ID = type_shelf[self.id],
            COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF = type_shelf[self.number_type_shelf],
            COLUMN_TYPE_SHELF_DEPTH = type_shelf[self.depth],
            COLUMN_TYPE_SHELF_HEIGHT = type_shelf[self.height],
            COLUMN_TYPE_SHELF_WIDTH = type_shelf[self.width],
            COLUMN_TYPE_SHELF_CREATION_DATE = type_shelf[self.creation_date]
        )
        return entity
    
    def lists(self, type_shelfs) -> list:
        if type_shelfs == None: 
            return type_shelfs
        return [self.type_shelf(type_shelf) for type_shelf in type_shelfs]
    
    def response(self, type_shelf) -> TypeShelfDto:
        if type_shelf == None: 
            return type_shelf
        return TypeShelfDto(
            COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF = type_shelf[self.number_type_shelf],
            COLUMN_TYPE_SHELF_DEPTH = type_shelf[self.depth],
            COLUMN_TYPE_SHELF_HEIGHT = type_shelf[self.height],
            COLUMN_TYPE_SHELF_WIDTH = type_shelf[self.width],
            COLUMN_TYPE_SHELF_CREATION_DATE = type_shelf[self.creation_date]
        )

    def type_shelf_dict(self, type_shelf, create= None) -> dict:
        if type_shelf == None: 
            return type_shelf
        try:
            id = type_shelf[self.id]
        except:
            id = None
        try:
            creation_date = type_shelf[self.creation_date]
        except:
            creation_date = None
        data = {
            self.number_type_shelf: type_shelf[self.number_type_shelf],
            self.depth: type_shelf[self.depth],
            self.height: type_shelf[self.height],
            self.width: type_shelf[self.width]
        }
        if id != None:
            data[self.id]= id
        if creation_date != None:
            data[self.creation_date]= creation_date
        if create != None:
            data[self.creation_date]= create
        return data