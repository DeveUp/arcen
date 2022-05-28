from sqlalchemy.orm import Session

from src.model.entity.Shelf import Shelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_SHELF, COLUMN_SHELF_ID

class UpdateTypeShelfRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_SHELF_ID]
        element = data[COLUMN_SHELF]
        element = self.db.query(Shelf).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element