from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_TYPE_FURNITURE_ID, COLUMN_TYPE_FURNITURE_ID_TWO

class DeleteByIdTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_type_furniture()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_TYPE_FURNITURE_ID_TWO])
        self.collection.find_one_and_delete({COLUMN_TYPE_FURNITURE_ID:id})
        return True