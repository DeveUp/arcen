from src.service.IService import IService

from src.persistence.repository.invoice.FindByIdInvoiceRepository import FindByIdInvoiceRepository
from src.persistence.schema.InvoiceSchema import InvoiceSchema

from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_INVOICE_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdInvoiceService(IService):

    def __init__(self):
        self.repository = FindByIdInvoiceRepository()
        self.schema = InvoiceSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_INVOICE_FIND_BY_ID_NOT_CONTENT)
        return element