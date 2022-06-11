from src.service.IService import IService

from src.persistence.repository.invoice_status.FindAllInvoiceStatusRepository import FindAllInvoiceStatusRepository
from src.persistence.schema.InvoiceStatusSchema import InvoiceStatusSchema

class FindAllInvoiceStatusService(IService):

    def __init__(self):
        self.repository = FindAllInvoiceStatusRepository()
        self.schema = InvoiceStatusSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)