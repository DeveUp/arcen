from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_INVOICE_STATUS_ID, COLUMN_INVOICE_STATUS_ID_TWO

class DeleteByIdInvoiceStatusRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_INVOICE_STATUS_ID_TWO])
        self.collection.find_one_and_delete({COLUMN_INVOICE_STATUS_ID:id})
        return True