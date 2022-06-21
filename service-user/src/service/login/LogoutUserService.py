from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.user.UpdateUserLoginRepository import UpdateUserLoginRepository
from src.persistence.repository.user.FindByIdUserRepository import FindByIdUserRepository
from src.persistence.schema.UserSchema import UserSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_USER_LOGOUT_ERROR
from src.util.constant import AUDIT_USER_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,COLUMN_USER,COLUMN_USER_ID,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception,  get_response_audit

class LogoutUserService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateUserLoginRepository(db)
        self.repositoryFind = FindByIdUserRepository(db)
        self.schema = UserSchema()

    def execute(self, data:dict):
        user = data.get("id")
        #print(data)
        elementFind = self.repositoryFind.execute(data)
        if elementFind != None:
            elementFind.session_started = False
        else:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT)
        print(elementFind.id)
        data = {
            COLUMN_USER_ID : elementFind.id,
            COLUMN_USER : elementFind
        }
        element = self.repository.execute(data)
        element = self.schema.response(element)
        return element