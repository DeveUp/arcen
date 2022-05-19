from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.repository.furniture.DeleteByIdFurnitureRepository import DeleteByIdFurnitureRepository
from src.util.constant import COLUMN_FURNITURE

class DeleteByIdFurnitureService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdFurnitureRepository(db)
        self.repository = DeleteByIdFurnitureRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_FURNITURE: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element