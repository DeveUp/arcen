from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject
from src.persistence.repository.IRepository import IRepository

class FindAllTypeObjectRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(TypeObject).all()