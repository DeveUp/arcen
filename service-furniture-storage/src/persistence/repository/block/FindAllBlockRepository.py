from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.BlockTable import BlockTable

class FindAllBlockRepository(IRepository):

    def __init__(self):
        table = BlockTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        return self.db.query(Block).all()