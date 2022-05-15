from src.service.IService import IService
from src.persistence.repository.block.DeleteByIdBlockRepository import DeleteByIdBlockRepository

class DeleteByIdBlockService(IService):

    def __init__(self):
        self.repository = DeleteByIdBlockRepository()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element