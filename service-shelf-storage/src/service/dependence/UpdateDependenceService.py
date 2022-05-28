from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Dependence.UpdateDependenceRepository import UpdateDependenceRepository
from src.persistence.schema.DependenceSchema import DependenceSchema

class UpdateDependenceService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateDependenceRepository(db)
        self.schema = DependenceSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.dependence(element)
        except:
            element= None
        return element