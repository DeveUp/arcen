from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_object.UpdateTypeObjectRepository import UpdateTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

class UpdateTypeObjectService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        return element