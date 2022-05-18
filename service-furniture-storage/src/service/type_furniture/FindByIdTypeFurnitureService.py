from src.service.IService import IService
from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class FindByIdTypeFurnitureService(IService):

    def __init__(self):
        self.repository = FindByIdTypeFurnitureRepository()
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.type_furniture(element)
        except:
            element= None
        return element