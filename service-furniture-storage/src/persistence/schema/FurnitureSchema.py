from src.model.entity.Furniture import Furniture
from src.model.dto.FurnitureDto import FurnitureDto
from src.util.constant import COLUMN_FURNITURE_ID, COLUMN_FURNITURE_ID_BLOCK, COLUMN_FURNITURE_ID_TYPE_FURNITURE, COLUMN_FURNITURE_NUMBER_FURNITURE, COLUMN_FURNITURE_CREATION_DATE

class FurnitureSchema:

    def __init__(self):
        self.id = COLUMN_FURNITURE_ID
        self.id_block = COLUMN_FURNITURE_ID_BLOCK
        self.id_type_furniture = COLUMN_FURNITURE_ID_TYPE_FURNITURE
        self.number_furniture = COLUMN_FURNITURE_NUMBER_FURNITURE
        self.creation_date = COLUMN_FURNITURE_CREATION_DATE

    def furniture(self, furniture) -> Furniture:
        if furniture == None: 
            return furniture
        return furniture

    def furniture_other(self, furniture) -> Furniture:
        if furniture == None: 
            return furniture
        entity = Furniture(
            COLUMN_FURNITURE_ID = furniture[self.id],
            COLUMN_FURNITURE_ID_BLOCK = furniture[self.id_block],
            COLUMN_FURNITURE_ID_TYPE_FURNITURE = furniture[self.id_type_furniture],
            COLUMN_FURNITURE_NUMBER_FURNITURE = furniture[self.number_furniture],
            COLUMN_FURNITURE_CREATION_DATE = furniture[self.creation_date]
        )
        return entity
    
    def furnitures(self, furnitures) -> list:
        if furnitures == None: 
            return furnitures
        return [self.furniture(furniture) for furniture in furnitures]
    
    def furniture_dto(self, furniture) -> FurnitureDto:
        if furniture == None: 
            return furniture
        return FurnitureDto(
            COLUMN_FURNITURE_ID_BLOCK = furniture[self.id_block], 
            COLUMN_FURNITURE_ID_TYPE_FURNITURE = furniture[self.id_type_furniture], 
            COLUMN_FURNITURE_NUMBER_FURNITURE = furniture[self.number_furniture], 
            COLUMN_FURNITURE_CREATION_DATE = furniture[self.creation_date]
        )

    def furniture_dict(self, furniture, create= None) -> dict:
        if furniture == None: 
            return furniture
        try:
            id = furniture[self.id]
        except:
            id = None
        try:
            creation_date = furniture[self.creation_date]
        except:
            creation_date = None
        data = {
            self.id_block: furniture[self.id_block],
            self.id_type_furniture: furniture[self.id_type_furniture],
            self.number_furniture: furniture[self.number_furniture]
        }
        if id != None:
            data[self.id]= id
        if creation_date != None:
            data[self.creation_date]= creation_date
        if create != None:
            data[self.creation_date]= create
        return data