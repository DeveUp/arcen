from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID

class UpdateFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_FURNITURE_ID]
        element = data[COLUMN_FURNITURE]
        element = self.db.query(Furniture).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element