from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository

class FindAllBoxRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(entity).all()