from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_ROLE_ID

class FindByIdUserRoleRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_USER_ROLE_ID]
        element = self.db.query(UserRole).filter(UserRole.id == id).first()
        return element