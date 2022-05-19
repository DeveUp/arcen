from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_FURNITURE

class SaveFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Furniture(**dict(data[COLUMN_FURNITURE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element