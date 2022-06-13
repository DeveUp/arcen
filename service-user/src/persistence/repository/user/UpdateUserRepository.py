from sqlalchemy.orm import Session

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER, COLUMN_USER_ID

class UpdateUserRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_USER_ID]
        element2 = data[COLUMN_USER]
        element = self.db.query(User).get(id)
        element.document=element2.document
        element.full_name=element2.full_name
        element.email=element2.email
        element.password=element2.password
        #element.status=element2.status
        #element.session_started=element2.session_started
        self.db.commit()
        self.db.refresh(element)
        return element