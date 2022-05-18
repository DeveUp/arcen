from src.model.entity.Block import Block
from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.BlockTable import BlockTable
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_LETTER, COLUMN_BLOCK_FLAT

class SaveBlockRepository(IRepository):

    def __init__(self):
        table = BlockTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        try:
            element = Block(**dict(data[COLUMN_BLOCK]))
            self.db.add(element)
            self.db.commit()
            self.db.refresh(element)
        except:
            element= None
        return element