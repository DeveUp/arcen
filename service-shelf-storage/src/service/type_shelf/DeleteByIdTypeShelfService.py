from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.FindByIdTypeShelfRepository import FindByIdTypeShelfRepository
from src.persistence.repository.TypeShelf.DeleteByIdTypeShelfRepository import DeleteByIdTypeShelfRepository
from src.util.constant import COLUMN_TYPE_SHELF

class DeleteByIdTypeShelfService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdTypeShelfRepository(db)
        self.repository = DeleteByIdTypeShelfRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_TYPE_SHELF: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element