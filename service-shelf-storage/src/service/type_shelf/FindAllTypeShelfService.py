from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.FindAllTypeShelfRepository import FindAllTypeShelfRepository as FindAllRepository
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema as EntitySchema

class FindAllTypeShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.entity(elements)
