from sqlalchemy.orm import Session
from src.util.common import get_http_exception,get_response_audit
from src.service.IService import IService
#from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.DependenceSchema import DependenceSchema as EntitySchema
from src.persistence.repository.Dependence.FindByIdDependenceRepository import FindByIdDependenceRepository as FindByRepository
from src.persistence.repository.Dependence.DeleteByIdDependenceRepository import DeleteByIdDependenceRepository as DeleteByIdRepository
from src.util.constant import COLUMN_DEPENDENCE,COLUMN_DEPENDENCE_ID,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_DEPENDENCE_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID


class DeleteByIdDependenceService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByRepository(db)
        self.repository = DeleteByIdRepository(db)
        #self.feign = AuditFeign()
        #self.schema = EntitySchema()

    def execute(self, data:dict):
        try:
            id= data[COLUMN_DEPENDENCE_ID] 
            find_by_id = self.find_by_id.execute(data)
            #data = dict({COLUMN_DEPENDENCE: element})
            data = {
                COLUMN_DEPENDENCE: find_by_id,
                COLUMN_DEPENDENCE_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE]= element
            #data[COLUMN_DEPENDENCE]=get_response_audit(self.schema.response(find_by_id))
        except:
            element =None
            data[DATA_REMOVE]= DATA_REMOVE_VALUE_DEFAULT
        finally:
            #self.feign.save(self.feign.build(AUDIT_DEPENDENCE_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        return element