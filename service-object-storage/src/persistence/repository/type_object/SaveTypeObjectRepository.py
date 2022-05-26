from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_OBJECT

class SaveTypeObjectRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = TypeObject(**dict(data[COLUMN_TYPE_OBJECT]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element