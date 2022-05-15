from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID_TWO

class SaveBlockRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.find_by_id = FindByIdBlockRepository()
        self.collection = self.db.get_db_block()

    def execute(self, data:dict):
        try:
            block = dict(data[COLUMN_BLOCK])
            id = self.collection.insert_one(block)
            data = dict({COLUMN_BLOCK_ID_TWO: id.inserted_id})
            block = self.find_by_id.execute(data)
        except:
            block= None
        return block