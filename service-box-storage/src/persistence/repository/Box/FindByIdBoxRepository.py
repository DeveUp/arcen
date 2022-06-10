from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BOX_ID

class FindByIdBoxRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_BOX_ID]
        element = self.db.query(entity).filter(entity.id == id).first()
        return element