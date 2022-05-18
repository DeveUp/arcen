from fastapi import Depends
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.FurnitureTable import FurnitureTable
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository

class DeleteByIdFurnitureRepository(IRepository):

    def __init__(self):
        table = FurnitureTable()
        self.find_by_id = FindByIdFurnitureRepository()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        element = self.find_by_id.execute(data)
        self.db.delete(element)
        self.db.commit()
        return True