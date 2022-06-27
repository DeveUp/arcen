"""
    @name - FindByIdTypeShelfRepository
    @description - Repositorio para consultar un type Shelf por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF_ID

class FindByIdTypeShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un type shelf por su pk
    # @parameter - data - Json con el pk del type shelf
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_TYPE_SHELF_ID]
        element = self.db.query(TypeShelf).filter(TypeShelf.id == id).first()
        return element