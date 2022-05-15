from src.model.entity.Furniture import Furniture
from src.model.dto.FurnitureDto import FurnitureDto
from src.util.constant import COLUMN_FURNITURE_ID, COLUMN_FURNITURE_ID_BLOCK, COLUMN_FURNITURE_ID_TYPE_FURNITURE, COLUMN_FURNITURE_NUMBER_FURNITURE, COLUMN_FURNITURE_DATE

class FurnitureSchema:

    def __init__(self):
        self.id = COLUMN_FURNITURE_ID
        self.id_block = COLUMN_FURNITURE_ID_BLOCK
        self.id_type_furniture = COLUMN_FURNITURE_ID_TYPE_FURNITURE
        self.number_furniture = COLUMN_FURNITURE_NUMBER_FURNITURE
        self.date = COLUMN_FURNITURE_DATE

    def furniture(self, furniture) -> Furniture:
        if furniture == None: 
            return furniture
        entity = Furniture()
        entity.set_id(str(furniture[self.id]))
        entity.set_id_block(furniture[self.id_block])
        entity.set_id_type_furniture(furniture[self.id_type_furniture])
        entity.set_number_furniture(furniture[self.number_furniture])
        entity.set_date(furniture[self.date])
        return entity
    
    def furnitures(self, furnitures) -> list:
        if furnitures == None: 
            return furnitures
        return [self.furniture(furniture) for furniture in furnitures]
    
    def furniture_dto(self, furniture) -> FurnitureDto:
        if furniture == None: 
            return furniture
        return FurnitureDto(
            id_block = furniture[self.id_block], 
            id_type_furniture = furniture[self.id_type_furniture], 
            number_furniture = furniture[self.number_furniture], 
            date = furniture[self.date]
        )

    def furniture_dict(self, furniture, create= None) -> dict:
        if furniture == None: 
            return furniture
        try:
            id = furniture[self.id]
        except:
            id = None
        try:
            date = furniture[self.date]
        except:
            date = None
        data = {
            self.id_block: furniture[self.id_block],
            self.id_type_furniture: furniture[self.id_type_furniture],
            self.number_furniture: furniture[self.number_furniture]
        }
        if id != None:
            data[self.id]= id
        if date != None:
            data[self.date]= date
        if create != None:
            data[self.date]= create
        return data