from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.type_object.FindAllTypeObjectRepository import FindAllTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

class FindAllTypeObjectService(IService):

    def __init__(self, db:Session):
        self.repository = FindAllTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements = list()
        return elements