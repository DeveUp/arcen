from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BOX

class SaveBoxRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_BOX]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element