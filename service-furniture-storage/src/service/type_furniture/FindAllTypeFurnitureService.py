from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_furniture.FindAllTypeFurnitureRepository import FindAllTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class FindAllTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)