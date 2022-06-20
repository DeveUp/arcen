from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.Dependence.SaveDependenceRepository import SaveDependenceRepository as SaveRepository
from src.persistence.schema.DependenceSchema import DependenceSchema as SchemaEntity
from src.util.common import get_http_exception,  get_response_audit
from src.util.constant import RESPONSE_MSG_DEPENDENCE_SAVE_ERROR_SAVE,RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_DEPENDENCE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE

class SaveDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = SaveRepository(db)
        self.schema = SchemaEntity()
        self.feign = AuditFeign()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element=None
        finally:
            self.feign.save(self.feign.build(AUDIT_DEPENDENCE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,  get_response_audit(element)));
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE,RESPONSE_MSG_DEPENDENCE_SAVE_ERROR_SAVE)
        return element