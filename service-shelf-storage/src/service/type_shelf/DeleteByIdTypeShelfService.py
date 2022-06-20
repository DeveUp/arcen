from sqlalchemy.orm import Session

from src.service.IService import IService
from src.util.common import get_http_exception,get_response_audit
from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema as EntitySchema
from src.persistence.repository.TypeShelf.FindByIdTypeShelfRepository import FindByIdTypeShelfRepository as FindByRepository
from src.persistence.repository.TypeShelf.DeleteByIdTypeShelfRepository import DeleteByIdTypeShelfRepository as DeleteByIdRepository
from src.util.constant import COLUMN_TYPE_SHELF,COLUMN_TYPE_SHELF_ID, RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_TYPE_SHELF_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID


class DeleteByIdTypeShelfService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByRepository(db)
        self.repository = DeleteByIdRepository(db)
        self.feign = AuditFeign()
        self.schema = EntitySchema()

    def execute(self, data:dict): 
        try:
            id= data[COLUMN_TYPE_SHELF_ID]
            find_by_id = self.find_by_id.execute(data)
            data = {
                COLUMN_TYPE_SHELF: find_by_id,
                COLUMN_TYPE_SHELF_ID : id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(data)
            data[DATA_REMOVE]= element
            data[COLUMN_TYPE_SHELF] = get_response_audit(self.schema.response(find_by_id))
        except:
            element= None
            data[DATA_REMOVE]= DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_TYPE_SHELF_SERVICE,AUDIT_GENERIC_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element ==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT)
            return element