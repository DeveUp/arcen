from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

from src.service.IService import IService
from src.persistence.repository.user.UpdateUserLoginRepository import UpdateUserLoginRepository
from src.persistence.repository.user.FindByEmailUserRepository import FindByEmailUserRepository
from src.persistence.schema.UserSchema import UserSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_USER_LOGIN_ERROR
from src.util.constant import AUDIT_USER_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,COLUMN_USER,COLUMN_USER_ID
from src.util.common import get_http_exception,  get_response_audit

class LoginUserService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateUserLoginRepository(db)
        self.repositoryFind = FindByEmailUserRepository(db)
        self.schema = UserSchema()

    def execute(self, data:dict):
        user = data.get("user")
        #print(data)
        elementFind = self.repositoryFind.execute(data)
        elementFind.session_started = True
        print(elementFind.id)
        data = {
            COLUMN_USER_ID : elementFind.id,
            COLUMN_USER : elementFind
        }
        matched = check_password_hash(elementFind.password, user.password)
        if elementFind.email==user.email and matched==True and elementFind.document==user.document:
            element = self.repository.execute(data)
        else:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_USER_LOGIN_ERROR)
        return element