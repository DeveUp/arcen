"""
    @name - FindByIdTypeBoxRepository
    @description - Repositorio para consultar un type box por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX_ID

class FindByIdTypeBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un type box por su pk
    # @parameter - data - Json con el pk del type box
    # @return - Any
    def execute(self, data:dict):
        id = data[COLUMN_TYPE_BOX_ID]
        element = self.db.query(TypeBox).filter(TypeBox.id == id).first()
        print(id)
        print(element)
        return element