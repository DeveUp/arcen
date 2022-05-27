from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Dependence.FindAllDependenceRepository import FindAllDependenceRepository
from src.persistence.schema.DependenceSchema import DependenceSchema

class FindAllDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllDependenceRepository(db)
        self.schema = DependenceSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.dependences(elements)
        except:
            elements= None
        return elements