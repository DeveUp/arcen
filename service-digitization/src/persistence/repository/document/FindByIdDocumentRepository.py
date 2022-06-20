"""
    @description - Repositorio documento operacion consultar por el pk del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-19
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.DigitizationDB import DigitizationDB

from src.util.constant import DATABASE

class FindByIdDocumentRepository(IRepository):

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.db = DigitizationDB()
        self.collection = self.db.get_db_document()
        self.data = DATABASE['table']['document']

    # @override
    # @method - Consulta un documento por el pk
    # @parameter - data - Json con el pk del documento
    # @return - PK
    def execute(self, data:dict):
        id = ObjectId(data[self.data['column'][0]])
        return self.collection.find_one({
            self.data['pk']:id
        })