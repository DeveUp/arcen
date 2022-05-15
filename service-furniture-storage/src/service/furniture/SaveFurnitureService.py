from datetime import datetime

from src.service.IService import IService
from src.persistence.repository.furniture.SaveFurnitureRepository import SaveFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema
from src.util.constant import COLUMN_FURNITURE, FORMAT_DATE

class SaveFurnitureService(IService):

    def __init__(self):
        self.repository = SaveFurnitureRepository()
        self.schema = FurnitureSchema()

    def execute(self, data:dict):
        try:
            date = str(datetime.today().strftime(FORMAT_DATE))
            furniture = self.schema.furniture_dict(dict(data[COLUMN_FURNITURE]), date)
            furniture = self.schema.furniture_dto(dict(furniture))
            data = dict({COLUMN_FURNITURE: furniture})
            element = self.schema.furniture(self.repository.execute(data))
        except:
            element= None
        return element