from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.role.FindAllRoleRepository import FindAllRoleRepository
from src.persistence.schema.RoleSchema import RoleSchema

class FindAllRoleService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRoleRepository(db)
        self.schema = RoleSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements