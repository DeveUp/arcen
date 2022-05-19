from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_FURNITURE

class SaveTypeFurnitureRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        element = TypeFurniture(**dict(data[COLUMN_TYPE_FURNITURE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element