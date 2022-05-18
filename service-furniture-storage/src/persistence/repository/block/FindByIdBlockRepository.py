from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.BlockTable import BlockTable
from src.util.constant import COLUMN_BLOCK_ID

class FindByIdBlockRepository(IRepository):

    def __init__(self):
        table = BlockTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        id = data[COLUMN_BLOCK_ID]
        element = self.db.query(Block).filter(Block.id == id).first()
        return element
       