from sqlalchemy.orm import Session

from src.model.entity.Role import Role
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_ROLE

class SaveRoleRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = Role(**dict(data[COLUMN_ROLE]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element