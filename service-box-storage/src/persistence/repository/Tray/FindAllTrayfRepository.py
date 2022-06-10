from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository

class FindAllTrayRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(entity).all()