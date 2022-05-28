from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Dependence.FindByIdDependenceRepository import FindByIdDependenceRepository
from src.persistence.schema.DependenceSchema import DependenceSchema

class FindByIdDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdDependenceRepository(db)
        self.schema = DependenceSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.dependence(element)
        except:
            element= None
        return element