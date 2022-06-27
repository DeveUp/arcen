"""
    @name - SaveUserRoleRepository
    @description - Repositorio para registrar un user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_ROLE

class SaveUserRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un user role
    # @parameter - data - Json con el user role a registrar
    # @return - UserRole
    def execute(self, data:dict):
        element = UserRole(**dict(data[COLUMN_USER_ROLE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element