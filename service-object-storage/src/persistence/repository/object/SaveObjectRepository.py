"""
    @name - SaveObjectRepository
    @description - Repositorio para registrar un objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Object import Object

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un objecto
    # @parameter - data - Json con el objecto a registrar
    # @return - Object
    def execute(self, data:dict):
        element = Object(**dict(data[DATABASE['table']['object']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element