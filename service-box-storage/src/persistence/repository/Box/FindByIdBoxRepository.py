"""
    @name - FindByIdBoxRepository
    @description - Repositorio para consultar una box por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BOX_ID

class FindByIdBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta una box por su pk
    # @parameter - data - Json con el pk del box
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_BOX_ID]
        element = self.db.query(entity).filter(entity.id == id).first()
        return element