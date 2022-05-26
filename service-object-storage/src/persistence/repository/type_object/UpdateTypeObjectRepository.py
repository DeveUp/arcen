from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_OBJECT, COLUMN_TYPE_OBJECT_ID

class UpdateTypeObjectRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_OBJECT_ID]
        element = data[COLUMN_TYPE_OBJECT]
        element = self.db.query(TypeObject).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element