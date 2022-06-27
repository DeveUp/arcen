"""
    @name - UserTable
    @description - Conexion a la tabla user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.Role import Base
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class UserTable(ITable):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        Base.metadata.create_all(bind=engine)

    # @override
    # @method - Realiza la conexion con la tabla user
    # @return - UserTable
    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()