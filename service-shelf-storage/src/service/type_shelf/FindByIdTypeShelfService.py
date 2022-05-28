from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.FindByIdTypeShelfRepository import FindByIdTypeShelfRepository
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema

class FindByIdTypeShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdTypeShelfRepository(db)
        self.schema = TypeShelfSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.type_shelf(element)
        except:
            element= None
        return element