from sqlalchemy.orm import Session

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF, COLUMN_TYPE_SHELF_ID

class UpdateTypeShelfRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_SHELF_ID]
        element = data[COLUMN_TYPE_SHELF]
        element = self.db.query(TypeShelf).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element