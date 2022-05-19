from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BLOCK_ID

class FindByIdBlockRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_BLOCK_ID]
        element = self.db.query(Block).filter(Block.id == id).first()
        return element
       