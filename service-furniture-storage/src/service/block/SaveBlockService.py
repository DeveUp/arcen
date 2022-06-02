from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.block.SaveBlockRepository import SaveBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_BLOCK_SAVE_ERROR_SAVE
from src.util.common import get_http_exception

class SaveBlockService(IService):

    def __init__(self, db: Session):
        self.repository = SaveBlockRepository(db)
        self.schema = BlockSchema()
        self.feign = AuditFeign()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element = None
        finally:
            self.feign.save(self.feign.build("BLOCK", "SAVE", "TEST"))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_BLOCK_SAVE_ERROR_SAVE)
        return element