"""
    @name - SaveBoxRepository
    @description - Repositorio para registrar una box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BOX

class SaveBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra una box
    # @parameter - data - Json con la box a registrar
    # @return - Box
    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_BOX]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element