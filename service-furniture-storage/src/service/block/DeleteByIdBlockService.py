from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.schema.BlockSchema import BlockSchema
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.repository.block.DeleteByIdBlockRepository import DeleteByIdBlockRepository
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_BLOCK_DELETE_BY_ID_NOT_CONTENT
from src.util.constant import AUDIT_BLOCK_SERVICE, AUDIT_BLOCK_OPERATION_DELETE_BY_ID
from src.util.common import get_http_exception, get_response_audit

class DeleteByIdBlockService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdBlockRepository(db)
        self.schema = BlockSchema()
        self.repository = DeleteByIdBlockRepository(db)
        self.feign = AuditFeign()

    def execute(self, data:dict): 
        try:
            id = data[COLUMN_BLOCK_ID]
            find_by_id_block = self.find_by_id.execute(data)
            data = {
                COLUMN_BLOCK: find_by_id_block,
                COLUMN_BLOCK_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE] = element
            data[COLUMN_BLOCK] = get_response_audit(self.schema.response(find_by_id_block))
        except:
            element = None
            data[DATA_REMOVE] = DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_BLOCK_SERVICE, AUDIT_BLOCK_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_BLOCK_DELETE_BY_ID_NOT_CONTENT)
        return element