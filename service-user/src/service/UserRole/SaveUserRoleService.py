"""
    @name - SaveUserRoleService
    @description - Servicio para registrar un user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session


from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.user_role.SaveUserRoleRepository import SaveUserRoleRepository
from src.service.role.FindByIdRoleService import FindByIdRoleService as FindByEntity1
from src.service.user.FindByIdUserService import FindByIdUserService as FindByEntity2
from src.feign.DependenceFeign import DependenceFeign
from src.persistence.schema.UserRoleSchema import UserRoleSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_ROLE_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_USER_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE ,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT
from src.util.constant import COLUMN_ROLE_ID,COLUMN_USER_ID,DEPENDENCE_SERVICE_HOST_URL,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception,  get_response_audit

class SaveUserRoleService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveUserRoleRepository(db)
        self.schema = UserRoleSchema()
        self.repositoryRole = FindByEntity1(db);
        self.repositoryUser = FindByEntity2(db);
        self.feign = AuditFeign()
        self.feign_dependence = DependenceFeign()

    # @override
    # @method - Registra un user role
    # @parameter - data - Json con el user role a registrar
    # @return - UserRole
    def execute(self, data:dict):
        userRole = data.get("user_role")
        roleId = userRole.id_role
        dataRole = dict({COLUMN_ROLE_ID:roleId})
        UserId = userRole.id_user
        dataUser = dict({COLUMN_USER_ID:UserId})
        c = self.feign_dependence.findByID(userRole.id_dependence)
        if self.repositoryRole.execute(dataRole) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryUser.execute(dataUser) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT)
        if c == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element = None
        finally:
            self.feign.save(self.feign.build(AUDIT_USER_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_ROLE_SAVE_ERROR_SAVE)
        return element