"""
    @name - FindByIdDependenceRepository
    @description - Repositorio para consultar un dependence por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE_ID

class FindByIdDependenceRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un dependence por su pk
    # @parameter - data - Json con el pk del dependence
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_DEPENDENCE_ID]
        element = self.db.query(Dependence).filter(Dependence.id == id).first()
        return element