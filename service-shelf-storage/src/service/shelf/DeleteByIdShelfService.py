from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.FindByIdShelfRepository import FindByIdShelfRepository
from src.persistence.repository.Shelf.DeleteByIdShelfRepository import DeleteByIdShelfRepository
from src.util.constant import COLUMN_SHELF

class DeleteByIdShelfService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdShelfRepository(db)
        self.repository = DeleteByIdShelfRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_SHELF: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element