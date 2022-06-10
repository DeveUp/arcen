from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_INVOICE_STATUS

class SaveInvoiceStatusRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice_status()

    def execute(self, data:dict):
        element = dict(data[COLUMN_INVOICE_STATUS])
        id = self.collection.insert_one(element)
        return id.inserted_id