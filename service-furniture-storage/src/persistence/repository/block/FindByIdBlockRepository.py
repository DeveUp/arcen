from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_BLOCK_ID, COLUMN_BLOCK_ID_TWO

class FindByIdBlockRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_block()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_BLOCK_ID_TWO])
        return self.collection.find_one({COLUMN_BLOCK_ID:id})
       