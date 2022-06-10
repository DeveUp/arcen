from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeBox.FindAllTypeBoxRepository import FindAllTypeBoxRepository as FindAllRepository
from src.persistence.schema.TypeBoxSchema import TypeBoxSchema as EntitySchema

class FindAllTypeBoxService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.lists(elements)
        