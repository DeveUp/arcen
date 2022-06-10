from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB

class FindAllInvoiceStatusRepository(IRepository):

    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_invoice_status()

    def execute(self, data:dict):
        return self.collection.find()