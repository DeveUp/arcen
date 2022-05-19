from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.furniture.FindAllFurnitureRepository import FindAllFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

class FindAllFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllFurnitureRepository(db)
        self.schema = FurnitureSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.furnitures(elements)
        except:
            elements= None
        return elements