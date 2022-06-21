"""
    @name - FindAllTypeFurnitureRepository
    @description - Repositorio para consultar todos los tipos de muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository

class FindAllTypeFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todos los tipos de muebles
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(TypeFurniture).all()