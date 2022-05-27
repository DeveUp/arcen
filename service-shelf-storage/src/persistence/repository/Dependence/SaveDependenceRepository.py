from sqlalchemy.orm import Session

from src.model.entity.Dependence import Dependence
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE

class SaveDependenceRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Dependence(**dict(data[COLUMN_DEPENDENCE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element