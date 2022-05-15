from src.persistence.repository.IRepository import IRepository

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB

class FindAllTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_type_furniture()

    def execute(self, data:dict):
        return self.collection.find()