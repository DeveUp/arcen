from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_DOCUMENT_ID, COLUMN_DOCUMENT_ID_TWO

class DeleteByIdDocumentRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_DOCUMENT_ID_TWO])
        self.collection.find_one_and_delete({COLUMN_DOCUMENT_ID:id})
        return True