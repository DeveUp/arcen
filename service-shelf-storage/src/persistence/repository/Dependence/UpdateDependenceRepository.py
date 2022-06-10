from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE, COLUMN_DEPENDENCE_ID

class UpdateDependenceRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_DEPENDENCE_ID]
        element2 = data[COLUMN_DEPENDENCE]
        element = self.db.query(Dependence).get(id)
        element.name = element2.name
        element.code = element2.code
        self.db.commit()
        self.db.refresh(element)
        return element