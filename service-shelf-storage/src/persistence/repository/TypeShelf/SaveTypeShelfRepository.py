from sqlalchemy.orm import Session
from pprint import pprint

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF

class SaveTypeShelfRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = TypeShelf(**dict(data[COLUMN_TYPE_SHELF]))
        #pprint(vars(element))
        self.db.add(element)
        self.db.commit()
        pprint(vars(element))
        self.db.refresh(element)
        return element