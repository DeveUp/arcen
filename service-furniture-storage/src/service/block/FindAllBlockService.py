from src.service.IService import IService
from src.persistence.repository.block.FindAllBlockRepository import FindAllBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

class FindAllBlockService(IService):

    def __init__(self):
        self.repository = FindAllBlockRepository()
        self.schema = BlockSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.blocks(elements)
        except:
            elements= None
        return elements