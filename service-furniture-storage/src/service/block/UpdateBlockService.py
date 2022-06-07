from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.block.UpdateBlockRepository import UpdateBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema
from src.util.constant import AUDIT_BLOCK_SERVICE, AUDIT_BLOCK_OPERATION_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_UPDATE_NOT_CONTENT, RESPONSE_MSG_BLOCK_UPDATE_NOT_CONTENT
from src.util.common import get_http_exception, get_response_audit

class UpdateBlockService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateBlockRepository(db)
        self.schema = BlockSchema()
        self.feign = AuditFeign()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
            print(element)
        except:
            element= None
        finally:
            self.feign.save(self.feign.build(AUDIT_BLOCK_SERVICE, AUDIT_BLOCK_OPERATION_UPDATE, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_UPDATE_NOT_CONTENT, RESPONSE_MSG_BLOCK_UPDATE_NOT_CONTENT)
        return element