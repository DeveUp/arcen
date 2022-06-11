from fastapi import HTTPException

from src.feign.AuditFeign import AuditFeign

from src.persistence.repository.document_location.SaveDocumentLocationRepository import SaveDocumentLocationRepository
from src.persistence.schema.DocumentLocationSchema import DocumentLocationSchema

from src.service.IService import IService
from src.service.document_location.FindByIdDocumentLocationService import FindByIdDocumentLocationService

from src.util.constant import COLUMN_DOCUMENT_LOCATION, COLUMN_DOCUMENT_LOCATION_ID_TWO
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_DOCUMENT_LOCATION_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_DOCUMENT_LOCATION_SERVICE, AUDIT_DOCUMENT_LOCATION_OPERATION_SAVE
from src.util.constant import DATA_COMMON_ERROR_CODE, DATA_COMMON_ERROR_MSG
from src.util.common import generate_date, get_http_exception, get_response_audit

class SaveDocumentLocationService(IService):

    def __init__(self):
        self.repository = SaveDocumentLocationRepository()
        self.findByIdAudit = FindByIdDocumentLocationService()
        self.schema = DocumentLocationSchema()
        self.feign_audit = AuditFeign()

    def execute(self, data:dict):
        try:
            document_location = self.schema.dict(dict(data[COLUMN_DOCUMENT_LOCATION]), generate_date())
            data = dict({COLUMN_DOCUMENT_LOCATION: self.schema.request(dict(document_location))})
            element = self.repository.execute(data)
        except HTTPException as error_http:
            self.error(error_http.status_code, error_http.detail)
        except:
            self.error(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_DOCUMENT_LOCATION_SAVE_ERROR_SAVE)
        # Find document location by id
        data = dict({COLUMN_DOCUMENT_LOCATION_ID_TWO: str(element)})
        element = self.findByIdAudit.execute(data)
        self.audit(element)
        return element

    def audit(self, response):
        return self.feign_audit.save(self.feign_audit.build(AUDIT_DOCUMENT_LOCATION_SERVICE, AUDIT_DOCUMENT_LOCATION_OPERATION_SAVE, get_response_audit(response)))
    
    def error(self, code, error):
        self.audit({
            DATA_COMMON_ERROR_CODE: code,
            DATA_COMMON_ERROR_MSG: error
        })
        raise get_http_exception(code, error)