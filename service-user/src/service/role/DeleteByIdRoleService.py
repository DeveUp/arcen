from sqlalchemy.orm import Session

#from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.role.FindByIdRoleRepository import FindByIdRoleRepository
from src.persistence.repository.role.DeleteByIdRoleRepository import DeleteByIdRoleRepository
from src.persistence.schema.RoleSchema import RoleSchema as EntitySchema
from src.util.constant import COLUMN_ROLE,COLUMN_ROLE_ID
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_ROLE_DELETE_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception,get_response_audit
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID

class DeleteByIdRoleService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdRoleRepository(db)
        self.repository = DeleteByIdRoleRepository(db)
        #self.feign = AuditFeign()
        self.schema = EntitySchema()

    def execute(self, data:dict): 
        try:
            id = data[COLUMN_ROLE_ID]
            find_by_id_role = self.find_by_id.execute(data)
            data = {
                COLUMN_ROLE: find_by_id_role,
                COLUMN_ROLE_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE] = element
            #data[COLUMN_ROLE] = get_response_audit(self.schema.response(find_by_id_role))
        except:
            element = None
            data[DATA_REMOVE] = DATA_REMOVE_VALUE_DEFAULT
        finally:
            #self.feign.save(self.feign.build(AUDIT_ROLE_SERVICE,AUDIT_GENERIC_OPERATION_DELETE_BY_ID,get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT, RESPONSE_MSG_ROLE_DELETE_BY_ID_NOT_CONTENT)
        return element