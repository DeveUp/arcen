from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE_ID

class FindByIdDependenceRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_DEPENDENCE_ID]
        element = self.db.query(Dependence).filter(Dependence.id == id).first()
        return element