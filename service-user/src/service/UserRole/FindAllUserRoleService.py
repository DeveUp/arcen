"""
    @name - FindAllUserRoleService
    @description - Servicio para consultar todos los user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.user_role.FindAllUserRoleRepository import FindAllUserRoleRepository
from src.persistence.schema.UserRoleSchema import UserRoleSchema

class FindAllUserRoleService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllUserRoleRepository(db)
        self.schema = UserRoleSchema()

    # @override
    # @method - Consulta todos los user role
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements