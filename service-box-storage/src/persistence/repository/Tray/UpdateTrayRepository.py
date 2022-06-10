from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY, COLUMN_TRAY_ID

class UpdateTrayRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TRAY_ID]
        element2 = data[COLUMN_TRAY]
        element = self.db.query(entity).get(id)
        element.id_shelf = element2.id_shelf
        element.height = element2.height
        element.width = element2.width
        element.depth = element2.depth
        self.db.commit()
        self.db.refresh(element)
        return element