from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID

class UpdateBlockRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_BLOCK_ID]
        element = data[COLUMN_BLOCK]
        element = self.db.query(Block).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element