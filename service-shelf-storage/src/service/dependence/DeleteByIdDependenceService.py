from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Dependence.FindByIdDependenceRepository import FindByIdDependenceRepository
from src.persistence.repository.Dependence.DeleteByIdDependeceRepository import DeleteByIdDependeceRepository
from src.util.constant import COLUMN_DEPENDENCE

class DeleteByIdDependenceService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdDependenceRepository(db)
        self.repository = DeleteByIdDependeceRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_DEPENDENCE: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element