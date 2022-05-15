from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_FURNITURE_ID, COLUMN_FURNITURE_ID_TWO

class FindByIdFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_furniture()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_FURNITURE_ID_TWO])
        return self.collection.find_one({COLUMN_FURNITURE_ID:id})
       