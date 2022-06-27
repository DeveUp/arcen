"""
    @name - FindByIdTrayRepository
    @description - Repositorio para consultar un tray por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY_ID

class FindByIdTrayRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un tray por su pk
    # @parameter - data - Json con el pk del tray
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_TRAY_ID]
        element = self.db.query(entity).filter(entity.id == id).first()
        return element