"""
    @name - UpdateDependenceRepository
    @description - Repositorio para actualizar un dependence por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE, COLUMN_DEPENDENCE_ID

class UpdateDependenceRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un dependence por su pk
    # @parameter - data - Json con el pk del dependence y el dependence a actualizar
    # @return - Dependence
    def execute(self, data:dict):
        id = data[COLUMN_DEPENDENCE_ID]
        element2 = data[COLUMN_DEPENDENCE]
        element = self.db.query(Dependence).get(id)
        element.name = element2.name
        element.code = element2.code
        self.db.commit()
        self.db.refresh(element)
        return element