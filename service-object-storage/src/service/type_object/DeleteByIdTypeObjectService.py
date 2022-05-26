from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_object.FindByIdTypeObjectRepository import FindByIdTypeObjectRepository
from src.persistence.repository.type_object.DeleteByIdTypeObjectRepository import DeleteByIdTypeObjectRepository
from src.util.constant import COLUMN_TYPE_OBJECT

class DeleteByIdTypeObjectService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdTypeObjectRepository(db)
        self.repository = DeleteByIdTypeObjectRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_TYPE_OBJECT: element})
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element