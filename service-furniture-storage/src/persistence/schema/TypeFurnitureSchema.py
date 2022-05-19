from src.model.entity.TypeFurniture import TypeFurniture
from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
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

    def type_furniture(self, type_furniture) -> TypeFurniture:
        if type_furniture == None: 
            return type_furniture
        return type_furniture

    def type_furniture_other(self, type_furniture) -> TypeFurniture:
        if type_furniture == None: 
            return type_furniture
        entity = TypeFurniture(
            COLUMN_TYPE_FURNITURE_ID = type_furniture[self.id],
            COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE = type_furniture[self.number_type_furniture],
            COLUMN_TYPE_FURNITURE_COUNT_RACK = type_furniture[self.count_rack],
            COLUMN_TYPE_FURNITURE_COUNT_ROW = type_furniture[self.count_row],
            COLUMN_TYPE_FURNITURE_DEPTH = type_furniture[self.depth],
            COLUMN_TYPE_FURNITURE_HEIGHT = type_furniture[self.height],
            COLUMN_TYPE_FURNITURE_WIDTH = type_furniture[self.width],
            COLUMN_TYPE_FURNITURE_CREATION_DATE = type_furniture[self.creation_date]
        )
        return entity
    
    def type_furnitures(self, type_furnitures) -> list:
        if type_furnitures == None: 
            return type_furnitures
        return [self.type_furniture(type_furniture) for type_furniture in type_furnitures]
    
    def type_furniture_dto(self, type_furniture) -> TypeFurnitureDto:
        if type_furniture == None: 
            return type_furniture
        return TypeFurnitureDto(
            COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE = type_furniture[self.number_type_furniture],
            COLUMN_TYPE_FURNITURE_COUNT_RACK = type_furniture[self.count_rack],
            COLUMN_TYPE_FURNITURE_COUNT_ROW = type_furniture[self.count_row],
            COLUMN_TYPE_FURNITURE_DEPTH = type_furniture[self.depth],
            COLUMN_TYPE_FURNITURE_HEIGHT = type_furniture[self.height],
            COLUMN_TYPE_FURNITURE_WIDTH = type_furniture[self.width],
            COLUMN_TYPE_FURNITURE_CREATION_DATE = type_furniture[self.creation_date]
        )

    def type_furniture_dict(self, type_furniture, create= None) -> dict:
        if type_furniture == None: 
            return type_furniture
        try:
            id = type_furniture[self.id]
        except:
            id = None
        try:
            creation_date = type_furniture[self.creation_date]
        except:
            creation_date = None
        data = {
            self.number_type_furniture: type_furniture[self.number_type_furniture],
            self.count_rack: type_furniture[self.count_rack],
            self.count_row: type_furniture[self.count_row],
            self.depth: type_furniture[self.depth],
            self.height: type_furniture[self.height],
            self.width: type_furniture[self.width]
        }
        if id != None:
            data[self.id]= id
        if creation_date != None:
            data[self.creation_date]= creation_date
        if create != None:
            data[self.creation_date]= create
        return data