"""
    @name - FindByIdSubObjectRepository
    @description - Repositorio para consultar un subobjeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.SubObject import SubObject

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class FindByIdSubObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un subobjeto por su pk
    # @parameter - data - Json con el pk del subobjeto
    # @return - Any
    def execute(self, data:dict):
        id = int(data[DATABASE['table']['subobject']['pk']])
        return self.db.query(SubObject).filter(SubObject.id == id).first()
       