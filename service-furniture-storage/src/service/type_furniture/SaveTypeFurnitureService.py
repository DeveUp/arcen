from datetime import datetime

from src.service.IService import IService
from src.persistence.repository.type_furniture.SaveTypeFurnitureRepository import SaveTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema
from src.util.constant import COLUMN_TYPE_FURNITURE, FORMAT_DATE

class SaveTypeFurnitureService(IService):

    def __init__(self):
        self.repository = SaveTypeFurnitureRepository()
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict):
        try:
            date = str(datetime.today().strftime(FORMAT_DATE))
            type_furniture = self.schema.type_furniture_dict(dict(data[COLUMN_TYPE_FURNITURE]), date)
            type_furniture = self.schema.type_furniture_dto(dict(type_furniture))
            data = dict({COLUMN_TYPE_FURNITURE: type_furniture})
            element = self.schema.type_furniture(self.repository.execute(data))
        except:
            element= None
        return element