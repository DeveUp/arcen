from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema
from src.service.IService import IService
from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.repository.type_furniture.DeleteByIdTypeFurnitureRepository import DeleteByIdTypeFurnitureRepository
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_TYPE_FURNITURE_DELETE_BY_ID_NOT_CONTENT
from src.util.constant import AUDIT_TYPE_FURNITURE_SERVICE, AUDIT_TYPE_FURNITURE_OPERATION_DELETE_BY_ID
from src.util.common import get_http_exception, get_response_audit

class DeleteByIdTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdTypeFurnitureRepository(db)
        self.repository = DeleteByIdTypeFurnitureRepository(db)
        self.feign = AuditFeign()
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict): 
        try:
            id = data[COLUMN_TYPE_FURNITURE_ID]
            find_by_id_type_furniture = self.find_by_id.execute(data)
            data = {
                COLUMN_TYPE_FURNITURE: find_by_id_type_furniture,
                COLUMN_TYPE_FURNITURE_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE] = element
            data[COLUMN_TYPE_FURNITURE] = get_response_audit(self.schema.response(find_by_id_type_furniture))
        except:
            element = None
            data[DATA_REMOVE] = DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_TYPE_FURNITURE_SERVICE, AUDIT_TYPE_FURNITURE_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_TYPE_FURNITURE_DELETE_BY_ID_NOT_CONTENT)
        return element