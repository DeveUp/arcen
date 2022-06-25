"""
    @name - SaveTypeShelfRepository
    @description - Repositorio para registrar un type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from pprint import pprint

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF

class SaveTypeShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un type shelf
    # @parameter - data - Json con el type shelf a registrar
    # @return - TypeShelf
    def execute(self, data:dict):
        element = TypeShelf(**dict(data[COLUMN_TYPE_SHELF]))
        #pprint(vars(element))
        self.db.add(element)
        self.db.commit()
        pprint(vars(element))
        self.db.refresh(element)
        return element