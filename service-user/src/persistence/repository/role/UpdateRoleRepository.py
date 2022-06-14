from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_ROLE, COLUMN_ROLE_ID

class UpdateRoleRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_ROLE_ID]
        element2 = data[COLUMN_ROLE]
        element = self.db.query(Role).get(id)
        element.name=element2.name
        self.db.commit()
        self.db.refresh(element)
        return element