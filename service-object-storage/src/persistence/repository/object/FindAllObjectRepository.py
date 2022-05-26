from sqlalchemy.orm import Session

from src.model.entity.Object import Object
from src.persistence.repository.IRepository import IRepository

class FindAllObjectRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(Object).all()