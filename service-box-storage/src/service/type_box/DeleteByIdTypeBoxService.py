from sqlalchemy.orm import Session
from src.util.common import get_http_exception,get_response_audit
from src.service.IService import IService
from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.TypeBoxSchema import TypeBoxSchema as EntitySchema
from src.persistence.repository.TypeBox.FindByIdTypeBoxRepository import FindByIdTypeBoxRepository as FindByRepository
from src.persistence.repository.TypeBox.DeleteByIdTypeBoxRepository import DeleteByIdTypeBoxRepository as DeleteByIdRepository
from src.util.constant import COLUMN_TYPE_BOX,COLUMN_TYPE_BOX_ID,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_TYPE_BOX_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID


class DeleteByIdTypeBoxService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByRepository(db)
        self.repository = DeleteByIdRepository(db)
        self.feign = AuditFeign()
        self.schema = EntitySchema()

    def execute(self, data:dict):
        id= data[COLUMN_TYPE_BOX_ID] 
        print(id)
        find_by_id = self.find_by_id.execute(data)
        print(find_by_id)
        try:
            id= data[COLUMN_TYPE_BOX_ID] 
            find_by_id = self.find_by_id.execute(data)
            #data = dict({COLUMN_DEPENDENCE: element})
            data = {
                COLUMN_TYPE_BOX: find_by_id,
                COLUMN_TYPE_BOX_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE]= element
            data[COLUMN_TYPE_BOX]=get_response_audit(self.schema.response(find_by_id))
        except:
            element =None
            data[DATA_REMOVE]= DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_TYPE_BOX_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT)
        return element