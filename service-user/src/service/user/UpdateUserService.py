from sqlalchemy.orm import Session

#from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.user.UpdateUserRepository import UpdateUserRepository
from src.persistence.schema.UserSchema import UserSchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import AUDIT_USER_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT

class UpdateUserService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateUserRepository(db)
        self.schema = UserSchema()
        #self.feing = AuditFeign()

    def execute(self, data:dict):
        try:
            print("Gregorio")
            element = self.repository.execute(data)
            
            print(vars(element))
            element = self.schema.entity(element)
        except:
            element= None
        finally:
            #self.feing.save(self.feing.build(AUDIT_USER_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE,get_response_audit(data)))
            if element==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT)
        return element