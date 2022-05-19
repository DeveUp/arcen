from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_furniture.UpdateTypeFurnitureRepository import UpdateTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

class UpdateTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.type_furniture(element)
        except:
            element= None
        return element