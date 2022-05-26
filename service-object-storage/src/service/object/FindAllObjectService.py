from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.object.FindAllObjectRepository import FindAllObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

class FindAllObjectService(IService):

    def __init__(self, db:Session):
        self.repository = FindAllObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements = list()
        return elements