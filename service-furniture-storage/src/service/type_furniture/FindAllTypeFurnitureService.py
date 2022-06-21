"""
    @name - FindAllTypeFurnitureService
    @description - Servicio para consultar todos los tipos de muebles
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.type_furniture.FindAllTypeFurnitureRepository import FindAllTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class FindAllTypeFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    # @override
    # @method - Consulta todos los tipos de muebles
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements = list()
        return elements