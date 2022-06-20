"""
    @name - FindAllSubObjectService
    @description - Servicio para consultar todos los subobjetos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.subobject.FindAllSubObjectRepository import FindAllSubObjectRepository
from src.persistence.schema.SubObjectSchema import SubObjectSchema

class FindAllSubObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.repository = FindAllSubObjectRepository(db)
        self.schema:SubObjectSchema = SubObjectSchema()

    # @override
    # @method - Consulta todos los subobjetos
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements = list()
        return elements