from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_ROLE

class SaveUserRoleRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = UserRole(**dict(data[COLUMN_USER_ROLE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element