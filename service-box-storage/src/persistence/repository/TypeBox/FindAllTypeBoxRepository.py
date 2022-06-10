from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox as entity
from src.persistence.repository.IRepository import IRepository

class FindAllTypeBoxRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(entity).all()