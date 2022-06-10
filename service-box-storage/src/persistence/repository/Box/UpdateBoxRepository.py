from sqlalchemy.orm import Session

from src.model.entity.Box import Box as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BOX, COLUMN_BOX_ID

class UpdateBoxRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_BOX_ID]
        element2 = data[COLUMN_BOX]
        element = self.db.query(entity).get(id)
        element.id_tray = element2.id_tray
        element.id_type_box = element2.id_type_box
        element.number_box = element2.number_box
        self.db.commit()
        self.db.refresh(element)
        return element