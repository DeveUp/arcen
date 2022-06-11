from src.service.IService import IService

from src.persistence.repository.invoice.FindAllInvoiceRepository import FindAllInvoiceRepository
from src.persistence.schema.InvoiceSchema import InvoiceSchema

class FindAllInvoiceService(IService):

    def __init__(self):
        self.repository = FindAllInvoiceRepository()
        self.schema = InvoiceSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)