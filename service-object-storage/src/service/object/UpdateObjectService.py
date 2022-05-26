from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.object.UpdateObjectRepository import UpdateObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

class UpdateObjectService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        return element