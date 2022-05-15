from src.service.IService import IService
from src.persistence.repository.furniture.DeleteByIdFurnitureRepository import DeleteByIdFurnitureRepository

class DeleteByIdFurnitureService(IService):

    def __init__(self):
        self.repository = DeleteByIdFurnitureRepository()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element