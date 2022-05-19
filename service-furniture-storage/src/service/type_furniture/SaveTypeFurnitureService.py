from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_furniture.SaveTypeFurnitureRepository import SaveTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class SaveTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = SaveTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.type_furniture(element)
        except:
            element= None
        return element