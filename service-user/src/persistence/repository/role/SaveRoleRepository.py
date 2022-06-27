"""
    @name - SaveRoleRepository
    @description - Repositorio para registrar un role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_ROLE

class SaveRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un role
    # @parameter - data - Json con el role a registrar
    # @return - Role
    def execute(self, data:dict):
        element = Role(**dict(data[COLUMN_ROLE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element