from sqlalchemy.orm import Session
import os
import httpx

#from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.user_role.SaveUserRoleRepository import SaveUserRoleRepository
from src.service.role.FindByIdRoleService import FindByIdRoleService as FindByEntity1
from src.service.user.FindByIdUserService import FindByIdUserService as FindByEntity2
from src.persistence.schema.UserRoleSchema import UserRoleSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_ROLE_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_USER_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE ,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT
from src.util.constant import COLUMN_ROLE_ID,COLUMN_USER_ID,DEPENDENCE_SERVICE_HOST_URL,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception,  get_response_audit

class SaveUserRoleService(IService):

    def __init__(self, db: Session):
        self.repository = SaveUserRoleRepository(db)
        self.schema = UserRoleSchema()
        self.repositoryRole = FindByEntity1(db);
        self.repositoryUser = FindByEntity2(db);
        #self.feign = AuditFeign()

    def execute(self, data:dict):
        userRole = data.get("user_role")
        roleId = userRole.id_role
        dataRole = dict({COLUMN_ROLE_ID:roleId})
        UserId = userRole.id_user
        dataUser = dict({COLUMN_USER_ID:UserId})
        url = os.environ.get('DEPENDENCE_SERVICE_HOST_URL') or DEPENDENCE_SERVICE_HOST_URL
        r = httpx.get(f'{url}{userRole.id_dependence}')
        c = True if r.status_code == 200 else False
        print(r)
        if self.repositoryRole.execute(dataRole) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryUser.execute(dataUser) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT)
        if c == False:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element = None
        finally:
            #self.feign.save(self.feign.build(AUDIT_USER_ROLE_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_USER_ROLE_SAVE_ERROR_SAVE)
        return element