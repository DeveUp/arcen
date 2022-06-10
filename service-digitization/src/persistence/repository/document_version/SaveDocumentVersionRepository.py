from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_DOCUMENT_VERSION

class SaveDocumentVersionRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document_version()

    def execute(self, data:dict):
        element = dict(data[COLUMN_DOCUMENT_VERSION])
        id = self.collection.insert_one(element)
        return id.inserted_id