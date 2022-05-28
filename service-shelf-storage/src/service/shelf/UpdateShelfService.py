from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.UpdateShelfRepository import UpdateShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema

class UpdateShelfService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.shelf(element)
        except:
            element= None
        return element