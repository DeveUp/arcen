from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID

class UpdateTypeFurnitureRepository(IRepository):

    def __init__(self, db: Session):
        self.db =  db

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_FURNITURE_ID]
        element = data[COLUMN_TYPE_FURNITURE]
        element = self.db.query(TypeFurniture).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element