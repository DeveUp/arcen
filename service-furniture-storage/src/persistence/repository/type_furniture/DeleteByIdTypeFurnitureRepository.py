from fastapi import Depends
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable
from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository

class DeleteByIdTypeFurnitureRepository(IRepository):

    def __init__(self):
        table = TypeFurnitureTable()
        self.find_by_id = FindByIdTypeFurnitureRepository()
        self.db: Session = Depends(table.execute())

    def execute(self, data:dict):
        element = self.find_by_id.execute(data)
        self.db.delete(element)
        self.db.commit()
        return True