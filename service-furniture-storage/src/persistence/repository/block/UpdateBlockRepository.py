from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID_TWO

class UpdateBlockRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_block()

    def execute(self, data:dict):
        id = data[COLUMN_BLOCK_ID_TWO]
        block = data[COLUMN_BLOCK]
        block = self.collection.find_one_and_update({
            COLUMN_BLOCK_ID_TWO: ObjectId(id)
        },{
            "$set": dict(block)
        })
        return block