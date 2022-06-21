from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER

class SaveUserRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = User(**dict(data[COLUMN_USER]))
        p = element.password
        element.password=generate_password_hash(p)
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element