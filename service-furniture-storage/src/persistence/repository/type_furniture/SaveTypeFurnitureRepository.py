from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable
from src.util.constant import COLUMN_TYPE_FURNITURE

class SaveTypeFurnitureRepository(IRepository):

    def __init__(self):
        table = TypeFurnitureTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        try:
            element = TypeFurniture(**dict(data[COLUMN_TYPE_FURNITURE]))
            self.db.add(element)
            self.db.commit()
            self.db.refresh(element)
        except:
            element= None
        return element