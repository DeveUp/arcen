"""
    @name - FindByIdRoleRepository
    @description - Repositorio para consultar un role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_ROLE_ID

class FindByIdRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un role por su pk
    # @parameter - data - Json con el pk del role
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_ROLE_ID]
        element = self.db.query(Role).filter(Role.id == id).first()
        return element