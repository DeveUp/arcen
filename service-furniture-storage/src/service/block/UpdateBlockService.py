from src.service.IService import IService
from src.persistence.repository.block.UpdateBlockRepository import UpdateBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

class UpdateBlockService(IService):

    def __init__(self):
        self.repository = UpdateBlockRepository()
        self.schema = BlockSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.block(element)
        except:
            element= None
        return element