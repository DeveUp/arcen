from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID_TWO

class UpdateFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_furniture()

    def execute(self, data:dict):
        id = data[COLUMN_FURNITURE_ID_TWO]
        furniture = data[COLUMN_FURNITURE]
        furniture = self.collection.find_one_and_update({
            COLUMN_FURNITURE_ID_TWO: ObjectId(id)
        },{
            "$set": dict(furniture)
        })
        return furniture