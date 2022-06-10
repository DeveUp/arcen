from sqlalchemy.orm import Session

#from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.Dependence.UpdateDependenceRepository import UpdateDependenceRepository as UpdateRepository
from src.persistence.schema.DependenceSchema import DependenceSchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT
from src.util.constant import AUDIT_DEPENDENCE_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE

class UpdateDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateRepository(db)
        self.schema = DependenceSchema()
        #self.feign = AuditFeign()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element=None
        finally:
            #self.feign.save(self.feign.build(AUDIT_DEPENDENCE_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE),get_response_audit(data))
            if element ==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        return element  