"""
    @name - FindByIdUserRepository
    @description - Repositorio para consultar un user role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_ROLE_ID

class FindByIdUserRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un user role por su pk
    # @parameter - data - Json con el pk del user role
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_USER_ROLE_ID]
        element = self.db.query(UserRole).filter(UserRole.id == id).first()
        return element