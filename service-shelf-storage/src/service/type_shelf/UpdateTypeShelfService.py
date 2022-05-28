from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.UpdateTypeShelfRepository import UpdateTypeShelfRepository
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema

class UpdateTypeShelfService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateTypeShelfRepository(db)
        self.schema = TypeShelfSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.type_shelf(element)
        except:
            element= None
        return element