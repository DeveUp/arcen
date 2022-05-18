from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.FurnitureTable import FurnitureTable

class FindAllFurnitureRepository(IRepository):

    def __init__(self):
        table = FurnitureTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        return self.db.query(Furniture).all()