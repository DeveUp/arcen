from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_furniture.FindAllTypeFurnitureRepository import FindAllTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class FindAllTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.type_furnitures(elements)
        except:
            elements= None
        return elements