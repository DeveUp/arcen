"""
    @name - UpdateBlockRepository
    @description - Repositorio para actualizar un bloque por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from xml.dom.minidom import Element
from sqlalchemy.orm import Session

from src.model.entity.Block import Block

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class UpdateBlockRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un bloque por su pk
    # @parameter - data - Json con el pk del bloque y el bloque a actualizar
    # @return - Block
    def execute(self, data:dict):
        id = data[DATABASE['table']['block']['pk']]
        element = data[DATABASE['table']['block']['name']]
        element = self.diff(element, self.db.query(Block).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element

    # @method - Actualiza la diferencia entre dos bloques
    # @parameter - element_new - Json con el bloque nuevo
    # @parameter - element - Json con la informacion bd
    # @return - Block
    def diff(self, element_new, element:Block):
        element.letter = element_new.letter
        element.flat = element_new.flat
        return element