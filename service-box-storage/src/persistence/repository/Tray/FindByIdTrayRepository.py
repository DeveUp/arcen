from sqlalchemy.orm import Session

from src.model.entity.Tray import Tray as entity
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TRAY_ID

class FindByIdTrayRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_TRAY_ID]
        element = self.db.query(entity).filter(entity.id == id).first()
        return element