from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.repository.block.DeleteByIdBlockRepository import DeleteByIdBlockRepository
from src.util.constant import COLUMN_BLOCK
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_BLOCK_DELETE_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class DeleteByIdBlockService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdBlockRepository(db)
        self.repository = DeleteByIdBlockRepository(db)
        self.feign = AuditFeign()

    def execute(self, data:dict): 
        try:
            element = self.find_by_id.execute(data)
            data = dict({COLUMN_BLOCK: element})
            element = self.repository.execute(data)
        except:
            element = None
        finally:
            self.feign.save(self.feign.build("BLOCK", "DELETE_BY_ID", "TEST"))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_BLOCK_DELETE_BY_ID_NOT_CONTENT)
        return element