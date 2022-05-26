from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_OBJECT_ID

class FindByIdTypeObjectRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_OBJECT_ID]
        element = self.db.query(TypeObject).filter(TypeObject.id == id).first()
        return element
       