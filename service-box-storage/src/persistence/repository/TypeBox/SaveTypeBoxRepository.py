"""
    @name - SaveTypeBoxRepository
    @description - Repositorio para registrar un type box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX

class SaveTypeBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un type box
    # @parameter - data - Json con el type box a registrar
    # @return - TypeBox
    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_TYPE_BOX]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element