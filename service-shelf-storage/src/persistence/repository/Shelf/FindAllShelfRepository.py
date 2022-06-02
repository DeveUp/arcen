from sqlalchemy.orm import Session

from src.model.entity.Shelf import Shelf
from src.persistence.repository.IRepository import IRepository

class FindAllShelfRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(Shelf).all()