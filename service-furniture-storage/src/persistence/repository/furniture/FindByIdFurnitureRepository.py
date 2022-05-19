from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_FURNITURE_ID

class FindByIdFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_FURNITURE_ID]
        element = self.db.query(Furniture).filter(Furniture.id == id).first()
        return element
       