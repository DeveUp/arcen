from sqlalchemy.orm import Session

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF, COLUMN_TYPE_SHELF_ID

class UpdateTypeShelfRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_SHELF_ID]
        element2 = data[COLUMN_TYPE_SHELF]
        element = self.db.query(TypeShelf).get(id)
        element.number_type_shelf = element2.number_type_shelf
        element.depth = element2.depth
        element.height = element2.height
        element.width = element2.width
        self.db.commit()
        self.db.refresh(element)
        return element