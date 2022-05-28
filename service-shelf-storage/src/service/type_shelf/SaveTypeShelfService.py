from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.TypeShelf.SaveTypeShelfRepository import SaveTypeShelfRepository
from src.persistence.schema.TypeShelfSchema import TypeShelfSchema

class SaveTypeShelfService(IService):

    def __init__(self, db: Session):
        self.repository = SaveTypeShelfRepository(db)
        self.schema = TypeShelfSchema()

    def execute(self, data:dict):
        try:
            #print(data)
            print("Ger")
            element = self.repository.execute(data)
            print("Ger")
            element = self.schema.type_shelf(element)
            print(element)
        except:
            element= None
        return element