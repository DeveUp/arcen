"""
    @name - SaveShelfRepository
    @description - Repositorio para registrar un shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Shelf import Shelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_SHELF

class SaveShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db
        
    # @override
    # @method - Registra un shelf
    # @parameter - data - Json con el shelf a registrar
    # @return - Shelf
    def execute(self, data:dict):
        element = Shelf(**dict(data[COLUMN_SHELF]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element