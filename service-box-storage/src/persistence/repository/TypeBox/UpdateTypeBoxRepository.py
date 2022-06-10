from sqlalchemy.orm import Session

from src.model.entity.TypeBox import TypeBox
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_BOX, COLUMN_TYPE_BOX_ID

class UpdateTypeBoxRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_BOX_ID]
        element2 = data[COLUMN_TYPE_BOX]
        element = self.db.query(TypeBox).get(id)
        element.number_type_box = element2.number_type_box
        element.height = element2.height
        element.width = element2.width
        element.depth = element2.depth
        self.db.commit()
        self.db.refresh(element)
        return element