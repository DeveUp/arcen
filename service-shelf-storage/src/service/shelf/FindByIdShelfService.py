from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.FindByIdShelfRepository import FindByIdShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema

class FindByIdShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.shelf(element)
        except:
            element= None
        return element