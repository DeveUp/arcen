"""
    @name - FindAllUserService
    @description - Servicio para consultar todos los user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.user.FindAllUserRepository import FindAllUserRepository
from src.persistence.schema.UserSchema import UserSchema

class FindAllUserService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllUserRepository(db)
        self.schema = UserSchema()

    # @override
    # @method - Consulta todos los user
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements