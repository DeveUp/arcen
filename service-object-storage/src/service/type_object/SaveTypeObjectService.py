from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_object.SaveTypeObjectRepository import SaveTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

class SaveTypeObjectService(IService):

    def __init__(self, db: Session):
        self.repository = SaveTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        return element