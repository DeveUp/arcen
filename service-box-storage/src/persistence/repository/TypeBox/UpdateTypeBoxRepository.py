"""
    @name - UpdateTypeBoxRepository
    @description - Repositorio para actualizar un type box por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX, COLUMN_TYPE_BOX_ID

class UpdateTypeBoxRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un type box por su pk
    # @parameter - data - Json con el pk del type box y el type box a actualizar
    # @return - TypeBox
    def execute(self, data:dict):
        id = data[COLUMN_TYPE_BOX_ID]
        element2 = data[COLUMN_TYPE_BOX]
        element = self.db.query(TypeBox).get(id)
        element.number_type_box = element2.number_type_box
        element.height = element2.height
        element.width = element2.width
        element.depth = element2.depth
        self.db.commit()
        self.db.refresh(element)
        return element