from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_INVOICE_ID_TWO, COLUMN_INVOICE_ID

class FindByIdInvoiceRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_INVOICE_ID_TWO])
        return self.collection.find_one({COLUMN_INVOICE_ID:id})