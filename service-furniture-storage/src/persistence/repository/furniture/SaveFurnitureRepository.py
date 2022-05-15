from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID_TWO

class SaveFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.find_by_id = FindByIdFurnitureRepository()
        self.collection = self.db.get_db_furniture()

    def execute(self, data:dict):
        try:
            furniture = dict(data[COLUMN_FURNITURE])
            id = self.collection.insert_one(furniture)
            data = dict({COLUMN_FURNITURE_ID_TWO: id.inserted_id})
            furniture = self.find_by_id.execute(data)
        except:
            furniture= None
        return furniture