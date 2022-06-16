from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class FindByIdAuditRepository - Repositorio Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()
        self.data = DATABASE['table']['audit']

    # @Overrride
    # @Method - Consulta una auditoria por su pk
    # @Parameter - data - {id} - Representa pk de la auditoria
    # @Return - Collection
    def execute(self, data:dict):
        id = ObjectId(data[self.data['column'][0]])
        return self.collection.find_one({self.data['pk']:id})
       