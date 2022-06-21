"""
    @name - SaveBlockRepository
    @description - Repositorio para registrar un bloque
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Block import Block

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveBlockRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un bloque
    # @parameter - data - Json con el bloque a registrar
    # @return - Block
    def execute(self, data:dict):
        element = Block(**dict(data[DATABASE['table']['block']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element