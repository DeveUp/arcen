from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable

class FindAllTypeFurnitureRepository(IRepository):

    def __init__(self):
        table = TypeFurnitureTable()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        return self.db.query(TypeFurniture).all()