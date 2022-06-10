from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Dependence.FindAllDependenceRepository import FindAllDependenceRepository as FindAllRepository
from src.persistence.schema.DependenceSchema import DependenceSchema as EntitySchema

class FindAllDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.lists(elements)
        