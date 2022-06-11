from src.service.IService import IService

from src.persistence.repository.invoice_status.FindByIdInvoiceStatusRepository import FindByIdInvoiceStatusRepository
from src.persistence.schema.InvoiceStatusSchema import InvoiceStatusSchema

from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_INVOICE_STATU_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdInvoiceStatusService(IService):

    def __init__(self):
        self.repository = FindByIdInvoiceStatusRepository()
        self.schema = InvoiceStatusSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_INVOICE_STATU_FIND_BY_ID_NOT_CONTENT)
        return element