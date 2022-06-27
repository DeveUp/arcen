"""
    @name - UpdateTrayRepository
    @description - Repositorio para actualizar un tray por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY, COLUMN_TRAY_ID

class UpdateTrayRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un tray por su pk
    # @parameter - data - Json con el pk del tray y el tray a actualizar
    # @return - Tray
    def execute(self, data:dict):
        id = data[COLUMN_TRAY_ID]
        element2 = data[COLUMN_TRAY]
        element = self.db.query(entity).get(id)
        element.id_shelf = element2.id_shelf
        element.height = element2.height
        element.width = element2.width
        element.depth = element2.depth
        self.db.commit()
        self.db.refresh(element)
        return element