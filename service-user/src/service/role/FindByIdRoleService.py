"""
    @name - FindByIdRoleService
    @description - Servicio para consultar un role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from src.util.common import get_http_exception
from src.service.IService import IService
from src.persistence.repository.role.FindByIdRoleRepository import FindByIdRoleRepository as FindByEntity
from src.persistence.schema.RoleSchema import RoleSchema as SchemaEntity
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT

class FindByIdRoleService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByEntity(db)
        self.schema = SchemaEntity()

    # @override
    # @method - Consulta un role por su pk
    # @parameter - data - No aplica
    # @return - Object
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT)
        return element 