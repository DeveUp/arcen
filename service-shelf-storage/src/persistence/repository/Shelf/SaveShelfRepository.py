from sqlalchemy.orm import Session

from src.model.entity.Shelf import Shelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_SHELF

class SaveShelfRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Shelf(**dict(data[COLUMN_SHELF]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element