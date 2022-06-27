"""
    @name - SaveDependenceRepository
    @description - Repositorio para registrar un dependence
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE

class SaveDependenceRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un Dependence
    # @parameter - data - Json con el dependence a registrar
    # @return - Dependence
    def execute(self, data:dict):
        element = Dependence(**dict(data[COLUMN_DEPENDENCE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element