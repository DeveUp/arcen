from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BLOCK

class SaveBlockRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Block(**dict(data[COLUMN_BLOCK]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element