from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository

class FindAllRoleRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        return self.db.query(Role).all()