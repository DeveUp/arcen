from sqlalchemy.orm import Session

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository

class FindAllUserRoleRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(UserRole).all()