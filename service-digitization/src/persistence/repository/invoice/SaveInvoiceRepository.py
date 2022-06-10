from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB
from src.util.constant import COLUMN_INVOICE

class SaveInvoiceRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice()

    def execute(self, data:dict):
        element = dict(data[COLUMN_INVOICE])
        id = self.collection.insert_one(element)
        return id.inserted_id