"""
    @name - FindAllUserRepository
    @description - Repositorio para consultar todos los user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository

class FindAllUserRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todas los user
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(User).all()