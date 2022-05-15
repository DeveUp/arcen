from src.model.entity.TypeFurniture import TypeFurniture
from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_COUNT_RACK, COLUMN_TYPE_FURNITURE_COUNT_ROW, COLUMN_TYPE_FURNITURE_DEPTH, COLUMN_TYPE_FURNITURE_HEIGHT, COLUMN_TYPE_FURNITURE_WIDTH, COLUMN_TYPE_FURNITURE_DATE

class TypeFurnitureSchema:

    def __init__(self):
        self.id = COLUMN_TYPE_FURNITURE_ID
        self.number_type_furniture = COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE
        self.count_rack = COLUMN_TYPE_FURNITURE_COUNT_RACK
        self.count_row = COLUMN_TYPE_FURNITURE_COUNT_ROW
        self.depth = COLUMN_TYPE_FURNITURE_DEPTH
        self.height = COLUMN_TYPE_FURNITURE_HEIGHT
        self.width = COLUMN_TYPE_FURNITURE_WIDTH
        self.date = COLUMN_TYPE_FURNITURE_DATE

    def type_furniture(self, type_furniture) -> TypeFurniture:
        if type_furniture == None: 
            return type_furniture
        entity = TypeFurniture()
        entity.set_id(str(type_furniture[self.id]))
        entity.set_number_type_furniture(type_furniture[self.number_type_furniture])
        entity.set_count_rack(type_furniture[self.count_rack])
        entity.set_count_row(type_furniture[self.count_row])
        entity.set_depth(type_furniture[self.depth])
        entity.set_height(type_furniture[self.height])
        entity.set_width(type_furniture[self.width])
        entity.set_date(type_furniture[self.date])
        return entity
    
    def type_furnitures(self, type_furnitures) -> list:
        if type_furnitures == None: 
            return type_furnitures
        return [self.type_furniture(type_furniture) for type_furniture in type_furnitures]
    
    def type_furniture_dto(self, type_furniture) -> TypeFurnitureDto:
        if type_furniture == None: 
            return type_furniture
        return TypeFurnitureDto(
            number_type_furniture = type_furniture[self.number_type_furniture], 
            count_rack = type_furniture[self.count_rack], 
            count_row = type_furniture[self.count_row], 
            depth = type_furniture[self.depth],
            height = type_furniture[self.height],
            width = type_furniture[self.width],
            date = type_furniture[self.date]
        )

    def type_furniture_dict(self, type_furniture, create= None) -> dict:
        if type_furniture == None: 
            return type_furniture
        try:
            id = type_furniture[self.id]
        except:
            id = None
        try:
            date = type_furniture[self.date]
        except:
            date = None
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
        if date != None:
            data[self.date]= date
        if create != None:
            data[self.date]= create
        return data