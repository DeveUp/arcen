from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.object.FindByIdObjectRepository import FindByIdObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

class FindByIdObjectService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        return element