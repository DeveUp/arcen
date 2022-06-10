from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_DOCUMENT_LOCATION, COLUMN_DOCUMENT_LOCATION_ID, COLUMN_DOCUMENT_LOCATION_ID_TWO

class UpdateDocumentLocationRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document_location()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_DOCUMENT_LOCATION_ID_TWO])
        element = data[COLUMN_DOCUMENT_LOCATION]
        id = self.collection.find_one_and_update({
            "_id": ObjectId(id)
        },{
            "$set": dict(element)
        })
        return self.collection.find_one({COLUMN_DOCUMENT_LOCATION_ID:id})