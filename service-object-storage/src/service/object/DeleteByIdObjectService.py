from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.object.FindByIdObjectRepository import FindByIdObjectRepository
from src.persistence.repository.object.DeleteByIdObjectRepository import DeleteByIdObjectRepository
from src.util.constant import COLUMN_OBJECT

class DeleteByIdObjectService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdObjectRepository(db)
        self.repository = DeleteByIdObjectRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_OBJECT: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element