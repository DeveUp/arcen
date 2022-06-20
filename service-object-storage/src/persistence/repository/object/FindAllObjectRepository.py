"""
    @name - FindAllObjectRepository
    @description - Repositorio para consultar todos los objectos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Object import Object
from src.persistence.repository.IRepository import IRepository

class FindAllObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todos los objectos
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(Object).all()