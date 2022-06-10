from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX

class SaveTypeBoxRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = entity(**dict(data[COLUMN_TYPE_BOX]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element