from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.FindAllTypeShelfRepository import FindAllTypeShelfRepository
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema

class FindAllTypeShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllTypeShelfRepository(db)
        self.schema = TypeShelfSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.type_shelfs(elements)
        except:
            elements= None
        return elements