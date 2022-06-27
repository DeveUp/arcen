"""
    @name - SaveUserRepository
    @description - Repositorio para registrar un user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER

class SaveUserRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un user
    # @parameter - data - Json con el user a registrar
    # @return - User
    def execute(self, data:dict):
        element = User(**dict(data[COLUMN_USER]))
        p = element.password
        element.password=generate_password_hash(p)
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element