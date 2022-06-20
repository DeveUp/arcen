"""
    @name - FindAllSubObjectRepository
    @description - Repositorio para consultar todos los subobjetos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.SubObject import SubObject

from src.persistence.repository.IRepository import IRepository

class FindAllSubObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todos los subobjetos
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(SubObject).all()