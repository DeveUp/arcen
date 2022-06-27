"""
    @name - TypeBoxTable
    @description - Conexion a la tabla type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.model.entity.TypeShelf import Base
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class TypeShelfTable(ITable):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        Base.metadata.create_all(bind=engine)

    # @override
    # @method - Realiza la conexion con la tabla type shelf
    # @return - TypeShelfTable
    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
           db.close()