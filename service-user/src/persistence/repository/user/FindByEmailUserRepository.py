"""
    @name - FindByEmailUserRepository
    @description - Repositorio para consultar un user por su email
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_EMAIL

class FindByEmailUserRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un user por su email
    # @parameter - data - Json con el email del user
    # @return - Any
    def execute(self, data:dict):
        user = data.get("user")
        email = user.email
        print(email)
        element = self.db.query(User).filter(User.email == email).first()
        return element