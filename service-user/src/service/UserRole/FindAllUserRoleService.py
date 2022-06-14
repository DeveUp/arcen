from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.user_role.FindAllUserRoleRepository import FindAllUserRoleRepository
from src.persistence.schema.UserRoleSchema import UserRoleSchema

class FindAllUserRoleService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllUserRoleRepository(db)
        self.schema = UserRoleSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements