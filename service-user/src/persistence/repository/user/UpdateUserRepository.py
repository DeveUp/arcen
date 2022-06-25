"""
    @name - UpdateUserRepository
    @description - Repositorio para actualizar un user por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.User import User
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER, COLUMN_USER_ID

class UpdateUserRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un user por su pk
    # @parameter - data - Json con el pk del user y el user a actualizar
    # @return - User
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