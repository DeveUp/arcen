from datetime import datetime

from src.service.IService import IService
from src.persistence.repository.block.SaveBlockRepository import SaveBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema
from src.util.constant import COLUMN_BLOCK, FORMAT_DATE

class SaveBlockService(IService):

    def __init__(self):
        self.repository = SaveBlockRepository()
        self.schema = BlockSchema()

    def execute(self, data:dict):
        try:
            date = str(datetime.today().strftime(FORMAT_DATE))
            block = self.schema.block_dict(dict(data[COLUMN_BLOCK]), date)
            block = self.schema.block_dto(dict(block))
            data = dict({COLUMN_BLOCK: block})
            element = self.schema.block(self.repository.execute(data))
        except:
            element= None
        return element