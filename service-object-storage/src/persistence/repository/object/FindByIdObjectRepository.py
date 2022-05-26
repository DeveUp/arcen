from sqlalchemy.orm import Session

from src.model.entity.Object import Object
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_OBJECT_ID

class FindByIdObjectRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_OBJECT_ID]
        element = self.db.query(Object).filter(Object.id == id).first()
        return element
       