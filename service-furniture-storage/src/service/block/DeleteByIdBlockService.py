from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.repository.block.DeleteByIdBlockRepository import DeleteByIdBlockRepository
from src.util.constant import COLUMN_BLOCK

class DeleteByIdBlockService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdBlockRepository(db)
        self.repository = DeleteByIdBlockRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_BLOCK: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element