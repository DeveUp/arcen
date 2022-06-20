"""
    @name - FindByIdObjectRepository
    @description - Repositorio para consultar un objecto por su pk
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

class FindByIdObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un objecto por su pk
    # @parameter - data - Json con el pk del objecto
    # @return - Any
    def execute(self, data:dict):
        id = data[DATABASE['table']['object']['pk']]
        element = self.db.query(Object).filter(Object.id == id).first()
        return element
       