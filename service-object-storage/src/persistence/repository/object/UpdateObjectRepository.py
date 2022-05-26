from sqlalchemy.orm import Session

from src.model.entity.Object import Object
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_OBJECT, COLUMN_OBJECT_ID

class UpdateObjectRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_OBJECT_ID]
        element = data[COLUMN_OBJECT]
        element = self.db.query(Object).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element