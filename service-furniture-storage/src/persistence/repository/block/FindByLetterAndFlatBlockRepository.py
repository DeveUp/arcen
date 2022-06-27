"""
    @name - FindByLetterAndFlatBlockRepository
    @description - Repositorio para consultar un bloque por la letra y piso.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Block import Block

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class FindByLetterAndFlatBlockRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un bloque por la letra y piso
    # @parameter - data - Json con la letra y piso
    # @return - Any
    def execute(self, data:dict):
        letter = data[DATABASE['table']['block']['column'][1]]
        flat = data[DATABASE['table']['block']['column'][2]]
        return self.db.query(Block).filter(Block.letter == letter).filter(Block.flat == flat).first()