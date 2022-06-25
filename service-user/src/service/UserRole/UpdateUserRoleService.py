"""
    @name - UpdateUserRoleService
    @description - Servicio para actualizar un user role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.user_role.UpdateUserRoleRepository import UpdateUserRoleRepository
from src.service.role.FindByIdRoleService import FindByIdRoleService as FindByEntity1
from src.service.user.FindByIdUserService import FindByIdUserService as FindByEntity2
from src.persistence.schema.UserRoleSchema import UserRoleSchema
from src.feign.DependenceFeign import DependenceFeign
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import AUDIT_USER_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT
from src.util.constant import COLUMN_ROLE_ID,COLUMN_USER_ID,DEPENDENCE_SERVICE_HOST_URL,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_ROLE_FIND_BY_ID_NOT_CONTENT

class UpdateUserRoleService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = UpdateUserRoleRepository(db)
        self.schema = UserRoleSchema()
        self.repositoryRole = FindByEntity1(db);
        self.repositoryUser = FindByEntity2(db);
        self.feing = AuditFeign()
        self.feign_dependence = DependenceFeign()

    # @override
    # @method - Actualizar un user role por su pk
    # @parameter - data - Json con el user role a actualizar
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
            element= None
        finally:
            self.feing.save(self.feing.build(AUDIT_USER_ROLE_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE,get_response_audit(data)))
            if element==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_ROLE_FIND_BY_ID_NOT_CONTENT)
        return element