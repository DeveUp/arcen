from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.database.StorageDB import StorageDB
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID_TWO

class SaveTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.find_by_id = FindByIdTypeFurnitureRepository()
        self.collection = self.db.get_db_type_furniture()

    def execute(self, data:dict):
        try:
            type_furniture = dict(data[COLUMN_TYPE_FURNITURE])
            id = self.collection.insert_one(type_furniture)
            data = dict({COLUMN_TYPE_FURNITURE_ID_TWO: id.inserted_id})
            type_furniture = self.find_by_id.execute(data)
        except:
            type_furniture= None
        return type_furniture