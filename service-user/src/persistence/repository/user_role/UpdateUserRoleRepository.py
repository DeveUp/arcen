"""
    @name - UpdateUserRoleRepository
    @description - Repositorio para actualizar un user role por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from datetime import datetime

from src.model.entity.UserRole import UserRole
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER_ROLE, COLUMN_USER_ROLE_ID

class UpdateUserRoleRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un user role por su email
    # @parameter - data - Json con el email del user role y el user role a actualizar
    # @return - User
    def execute(self, data:dict):
        id = data[COLUMN_USER_ROLE_ID]
        element2 = data[COLUMN_USER_ROLE]
        element = self.db.query(UserRole).get(id)
        element.id_role=element2.id_role
        element.id_user=element2.id_user
        element.id_dependence=element2.id_dependence
        #element.status=element2.status
        #if element2.status == False:
            #element.date_end=datetime.utcnow
        self.db.commit()
        self.db.refresh(element)
        return element