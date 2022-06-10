from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX_ID

class FindByIdTypeBoxRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_BOX_ID]
        element = self.db.query(TypeBox).filter(TypeBox.id == id).first()
        print(id)
        print(element)
        return element