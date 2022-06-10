from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY

class SaveTrayRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_TRAY]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element