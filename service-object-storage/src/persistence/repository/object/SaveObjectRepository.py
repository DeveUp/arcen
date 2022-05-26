from sqlalchemy.orm import Session

from src.model.entity.Object import Object
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_OBJECT

class SaveObjectRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Object(**dict(data[COLUMN_OBJECT]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element