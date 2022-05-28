from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.FindAllShelfRepository import FindAllShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema

class FindAllShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.shelfs(elements)
        except:
            elements= None
        return elements