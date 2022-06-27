"""
    @name - FindAllBoxRepository
    @description - Repositorio para consultar todas las box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository

class FindAllBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todas las box
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(entity).all()