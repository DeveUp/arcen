"""
    @name - UpdateTypeShelfRepository
    @description - Repositorio para actualizar un type shelf por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF, COLUMN_TYPE_SHELF_ID

class UpdateTypeShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un type shelf por su pk
    # @parameter - data - Json con el pk del type shelf y el type shelf a actualizar
    # @return - TypeShelf
    def execute(self, data:dict):
        id = data[COLUMN_TYPE_SHELF_ID]
        element2 = data[COLUMN_TYPE_SHELF]
        element = self.db.query(TypeShelf).get(id)
        element.number_type_shelf = element2.number_type_shelf
        element.depth = element2.depth
        element.height = element2.height
        element.width = element2.width
        self.db.commit()
        self.db.refresh(element)
        return element