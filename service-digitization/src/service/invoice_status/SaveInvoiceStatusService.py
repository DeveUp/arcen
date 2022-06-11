from fastapi import HTTPException

from src.feign.AuditFeign import AuditFeign

from src.persistence.repository.invoice_status.SaveInvoiceStatusRepository import SaveInvoiceStatusRepository
from src.persistence.schema.InvoiceStatusSchema import InvoiceStatusSchema

from src.service.IService import IService
from src.service.invoice_status.FindByIdInvoiceStatusService import FindByIdInvoiceStatusService

from src.util.constant import COLUMN_INVOICE_STATUS, COLUMN_INVOICE_STATUS_ID_TWO
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_INVOICE_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_INVOICE_STATU_SERVICE, AUDIT_INVOICE_STATUS_OPERATION_SAVE
from src.util.constant import DATA_COMMON_ERROR_CODE, DATA_COMMON_ERROR_MSG
from src.util.common import generate_date, get_http_exception, get_response_audit

class SaveInvoiceStatusService(IService):

    def __init__(self):
        self.repository = SaveInvoiceStatusRepository()
        self.find_by_id_invoice_status = FindByIdInvoiceStatusService()
        self.schema = InvoiceStatusSchema()
        self.feign_audit = AuditFeign()

    def execute(self, data:dict):
        try:
            document = self.schema.dict(dict(data[COLUMN_INVOICE_STATUS]), generate_date())
            data = dict({COLUMN_INVOICE_STATUS: self.schema.request(dict(document))})
            element = self.repository.execute(data)
        except HTTPException as error_http:
            self.error(error_http.status_code, error_http.detail)
        except:
            self.error(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_INVOICE_SAVE_ERROR_SAVE)
        # Find document by id
        data = dict({COLUMN_INVOICE_STATUS_ID_TWO: str(element)})
        element = self.find_by_id_invoice_status.execute(data)
        self.audit(element)
        return element

    def audit(self, response):
        return self.feign_audit.save(self.feign_audit.build(AUDIT_INVOICE_STATU_SERVICE, AUDIT_INVOICE_STATUS_OPERATION_SAVE, get_response_audit(response)))
    
    def error(self, code, error):
        self.audit({
            DATA_COMMON_ERROR_CODE: code,
            DATA_COMMON_ERROR_MSG: error
        })
        raise get_http_exception(code, error)