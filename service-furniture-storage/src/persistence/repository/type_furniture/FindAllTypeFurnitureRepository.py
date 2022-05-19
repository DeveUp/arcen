from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository

class FindAllTypeFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(TypeFurniture).all()