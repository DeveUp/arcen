from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

class FindByIdFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdFurnitureRepository(db)
        self.schema = FurnitureSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.furniture(element)
        except:
            element= None
        return element