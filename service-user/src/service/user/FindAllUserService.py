from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.user.FindAllUserRepository import FindAllUserRepository
from src.persistence.schema.UserSchema import UserSchema

class FindAllUserService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllUserRepository(db)
        self.schema = UserSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements