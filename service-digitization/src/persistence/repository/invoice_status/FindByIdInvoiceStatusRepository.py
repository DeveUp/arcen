from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_INVOICE_STATUS_ID, COLUMN_INVOICE_STATUS_ID_TWO

class FindByIdInvoiceStatusRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice_status()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_INVOICE_STATUS_ID_TWO])
        return self.collection.find_one({COLUMN_INVOICE_STATUS_ID:id})