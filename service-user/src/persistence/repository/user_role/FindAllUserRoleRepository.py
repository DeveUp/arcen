"""
    @name - FindAllUserRoleRepository
    @description - Repositorio para consultar todos los user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository

class FindAllUserRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todas los user role
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(UserRole).all()