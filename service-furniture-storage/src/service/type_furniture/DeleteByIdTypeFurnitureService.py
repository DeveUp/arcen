from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.repository.type_furniture.DeleteByIdTypeFurnitureRepository import DeleteByIdTypeFurnitureRepository
from src.util.constant import COLUMN_TYPE_FURNITURE

class DeleteByIdTypeFurnitureService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdTypeFurnitureRepository(db)
        self.repository = DeleteByIdTypeFurnitureRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_TYPE_FURNITURE: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element