from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.SaveShelfRepository import SaveShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema

class SaveShelfService(IService):

    def __init__(self, db: Session):
        self.repository = SaveShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.shelf(element)
        except:
            element= None
        return 