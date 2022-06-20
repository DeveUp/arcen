"""
    @name - SaveTypeObjectRepository
    @description - Repositorio para registrar un tipo de objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveTypeObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un tipo de objecto
    # @parameter - data - Json con el tipo de objecto a registrar
    # @return - TypeObject
    def execute(self, data:dict):
        element = TypeObject(**dict(data[DATABASE['table']['type_object']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element