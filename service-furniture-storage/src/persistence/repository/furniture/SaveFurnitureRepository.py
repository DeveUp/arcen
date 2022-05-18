from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.FurnitureTable import FurnitureTable
from src.util.constant import COLUMN_FURNITURE

class SaveFurnitureRepository(IRepository):

    def __init__(self):
        table = FurnitureTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        try:
            element = Furniture(**dict(data[COLUMN_FURNITURE]))
            self.db.add(element)
            self.db.commit()
            self.db.refresh(element)
        except:
            element= None
        return element