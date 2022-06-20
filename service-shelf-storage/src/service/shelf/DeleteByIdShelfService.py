from sqlalchemy.orm import Session
from src.util.common import get_http_exception,get_response_audit
from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.schema.ShelfSchema import ShelfSchema as EntitySchema
from src.persistence.repository.Shelf.FindByIdShelfRepository import FindByIdShelfRepository as FindByIdRepository
from src.persistence.repository.Shelf.DeleteByIdShelfRepository import DeleteByIdShelfRepository as DeleteByIdRepository
from src.util.constant import COLUMN_SHELF,COLUMN_SHELF_ID, RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_SHELF_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID

class DeleteByIdShelfService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdRepository(db)
        self.repository = DeleteByIdRepository(db)
        self.feign = AuditFeign()
        self.schema = EntitySchema()

    def execute(self, data:dict): 
        try:
            id= data[COLUMN_SHELF_ID]
            find_by_id_entity = self.find_by_id.execute(data)
            data = {
                COLUMN_SHELF: find_by_id_entity,
                COLUMN_SHELF_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE] = element
            data[COLUMN_SHELF]=get_response_audit(self.schema.response(find_by_id_entity))
            print("data Gregori")
            print(data)
        except:
            element =None
            data[DATA_REMOVE]= DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_SHELF_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        