"""
    @name - UpdateShelfRepository
    @description - Repositorio para actualizar un shelf por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Shelf import Shelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_SHELF, COLUMN_SHELF_ID

class UpdateShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un shelf por su pk
    # @parameter - data - Json con el pk del shelf y el shelf a actualizar
    # @return - Shelf
    def execute(self, data:dict):
        id = data[COLUMN_SHELF_ID]
        print(id)
        element2 = data[COLUMN_SHELF]
        element = self.db.query(Shelf).get(id)
        print(vars(element))
        element.id_type_shelf = element2.id_type_shelf
        element.id_dependence = element2.id_dependence
        element.id_furniture = element2.id_furniture
        element.number_shelf = element2.number_shelf
        self.db.commit()
        self.db.refresh(element)
        return element