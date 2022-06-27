"""
    @name - SaveUserService
    @description - Servicio para registrar un user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.user.SaveUserRepository import SaveUserRepository
from src.persistence.schema.UserSchema import UserSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_USER_SERVICE, AUDIT_GENERIC_OPERATION_SAVE
from src.util.common import get_http_exception,  get_response_audit

class SaveUserService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveUserRepository(db)
        self.schema = UserSchema()
        self.feign = AuditFeign()

    # @override
    # @method - Registra un user
    # @parameter - data - Json con el user a registrar
    # @return - User
    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element = None
        finally:
            self.feign.save(self.feign.build(AUDIT_USER_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_SAVE_ERROR_SAVE)
        return element