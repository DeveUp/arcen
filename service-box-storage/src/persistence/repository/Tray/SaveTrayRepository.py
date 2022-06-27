"""
    @name - SaveTrayRepository
    @description - Repositorio para registrar un tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY

class SaveTrayRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un tray
    # @parameter - data - Json con el tray a registrar
    # @return - Tray
    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_TRAY]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element