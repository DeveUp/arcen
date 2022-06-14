from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_ROLE_ID

class FindByIdRoleRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_ROLE_ID]
        element = self.db.query(Role).filter(Role.id == id).first()
        return element