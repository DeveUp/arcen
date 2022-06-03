from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.FurnitureSchema import FurnitureSchema
from src.service.IService import IService
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.repository.furniture.DeleteByIdFurnitureRepository import DeleteByIdFurnitureRepository
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_FURNITURE_SERVICE, AUDIT_FURNITURE_OPERATION_DELETE_BY_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_FURNITURE_DELETE_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception, get_response_audit

class DeleteByIdFurnitureService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdFurnitureRepository(db)
        self.repository = DeleteByIdFurnitureRepository(db)
        self.feign = AuditFeign()
        self.schema = FurnitureSchema()

    def execute(self, data:dict): 
        try:
            id = data[COLUMN_FURNITURE_ID]
            find_by_id_furniture = self.find_by_id.execute(data)
            data = {
                COLUMN_FURNITURE: find_by_id_furniture,
                COLUMN_FURNITURE_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE] = element
            data[COLUMN_FURNITURE] = get_response_audit(self.schema.response(find_by_id_furniture))
        except:
            element = None
            data[DATA_REMOVE] = DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_FURNITURE_SERVICE, AUDIT_FURNITURE_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_FURNITURE_DELETE_BY_ID_NOT_CONTENT)
        return element