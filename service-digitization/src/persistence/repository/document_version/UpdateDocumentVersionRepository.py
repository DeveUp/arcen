from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_DOCUMENT_VERSION, COLUMN_DOCUMENT_VERSION_ID, COLUMN_DOCUMENT_VERSION_ID_TWO

class UpdateDocumentVersionRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document_version()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_DOCUMENT_VERSION_ID_TWO])
        element = data[COLUMN_DOCUMENT_VERSION]
        id = self.collection.find_one_and_update({
            "_id": ObjectId(id)
        },{
            "$set": dict(element)
        })
        return self.collection.find_one({COLUMN_DOCUMENT_VERSION_ID:id})