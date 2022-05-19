from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository

class FindAllFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db =  db

    def execute(self, data:dict):
        return self.db.query(Furniture).all()