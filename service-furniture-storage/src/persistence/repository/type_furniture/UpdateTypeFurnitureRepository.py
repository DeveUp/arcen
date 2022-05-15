from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID_TWO

class UpdateTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_type_furniture()

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_FURNITURE_ID_TWO]
        type_furniture = data[COLUMN_TYPE_FURNITURE]
        type_furniture = self.collection.find_one_and_update({
            COLUMN_TYPE_FURNITURE_ID_TWO: ObjectId(id)
        },{
            "$set": dict(type_furniture)
        })
        return type_furniture