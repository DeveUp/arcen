from fastapi import Depends
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.database.table.BlockTable import BlockTable

class DeleteByIdBlockRepository(IRepository):

    def __init__(self):
        table = BlockTable()
        self.find_by_id = FindByIdBlockRepository()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        element = self.find_by_id.execute(data)
        self.db.delete(element)
        self.db.commit()
        return True