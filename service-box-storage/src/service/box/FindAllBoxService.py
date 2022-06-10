from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Box.FindAllBoxRepository import FindAllBoxRepository as FindAllRepository
from src.persistence.schema.BoxSchema import BoxSchema as EntitySchema

class FindAllBoxService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.lists(elements)
        