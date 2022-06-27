"""
    @name - FindAllRoleService
    @description - Servicio para consultar todos los role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.role.FindAllRoleRepository import FindAllRoleRepository
from src.persistence.schema.RoleSchema import RoleSchema

class FindAllRoleService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllRoleRepository(db)
        self.schema = RoleSchema()

    # @override
    # @method - Consulta todos los role
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements