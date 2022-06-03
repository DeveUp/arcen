from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.service.block.FindByIdBlockService import FindByIdBlockService
from src.persistence.repository.furniture.SaveFurnitureRepository import SaveFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_FURNITURE_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_FURNITURE_SERVICE, AUDIT_FURNITURE_OPERATION_SAVE
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID_BLOCK
from src.util.constant import COLUMN_BLOCK_ID
from src.util.common import get_http_exception, get_response_audit

class SaveFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = SaveFurnitureRepository(db)
        self.find_by_id_block = FindByIdBlockService(db)
        self.schema = FurnitureSchema()
        self.feign = AuditFeign()

    def execute(self, data:dict):
        self.find_by_id_block.execute(dict({
            COLUMN_BLOCK_ID: str(data[COLUMN_FURNITURE].id_block)
        }))
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element = None
        finally:
            self.feign.save(self.feign.build(AUDIT_FURNITURE_SERVICE, AUDIT_FURNITURE_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_FURNITURE_SAVE_ERROR_SAVE)
        return element