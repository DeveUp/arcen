from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.furniture.UpdateFurnitureRepository import UpdateFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

class UpdateFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateFurnitureRepository(db)
        self.schema = FurnitureSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.furniture(element)
        except:
            element= None
        return element