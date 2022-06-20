from sqlalchemy.orm import Session

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_EMAIL

class FindByEmailUserRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        user = data.get("user")
        email = user.email
        print(email)
        element = self.db.query(User).filter(User.email == email).first()
        return element