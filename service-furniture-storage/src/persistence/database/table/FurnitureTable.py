"""
    @name - FurnitureTable
    @description - Conexion a la tabla mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.Furniture import Furniture
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class FurnitureTable(ITable):

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        Furniture.metadata.create_all(bind=engine)

    # @override
    # @method - Realiza la conexion con la tabla mueble
    # @return - FurnitureTable
    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()