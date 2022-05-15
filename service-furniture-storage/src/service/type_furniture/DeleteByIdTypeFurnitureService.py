from src.service.IService import IService
from src.persistence.repository.type_furniture.DeleteByIdTypeFurnitureRepository import DeleteByIdTypeFurnitureRepository

class DeleteByIdTypeFurnitureService(IService):

    def __init__(self):
        self.repository = DeleteByIdTypeFurnitureRepository()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element