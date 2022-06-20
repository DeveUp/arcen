"""
    @description - Repositorio documento operacion registrar documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB

from src.util.constant import DATABASE

class SaveDocumentRepository(IRepository):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document()

    # @override
    # @method - Registra una documento
    # @parameter - data - Json con el documento
    # @return - PK
    def execute(self, data:dict):
        element = dict(data[DATABASE['table']['document']['name']])
        id = self.collection.insert_one(element)
        return id.inserted_id