from src.service.IService import IService
from src.persistence.repository.furniture.SaveFurnitureRepository import SaveFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

class SaveFurnitureService(IService):

    def __init__(self):
        self.repository = SaveFurnitureRepository()
        self.schema = FurnitureSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.furniture(element)
        except:
            element= None
        return element