from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB

class FindAllDocumentRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document()

    def execute(self, data:dict):
        return self.collection.find()