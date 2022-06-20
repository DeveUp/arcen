"""
    @name - SaveSubObjectRepository
    @description - Repositorio para registrar un subobjeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from ast import Sub
from sqlalchemy.orm import Session

from src.model.entity.SubObject import SubObject

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveSubObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un subobjeto
    # @parameter - data - Json con el subobjeto a registrar
    # @return - SubObject
    def execute(self, data:dict):
        element = SubObject(**dict(data[DATABASE['table']['subobject']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element