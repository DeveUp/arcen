from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_object.FindByIdTypeObjectRepository import FindByIdTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

class FindByIdTypeObjectService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        return element