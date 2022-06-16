from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class SaveAuditRepository - Repositorio Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    # @Overrride
    # @Method - Registra una auditoria
    # @Parameter - data - {audit} - Representa la auditoria
    # @Return - PK
    def execute(self, data:dict):
        audit = dict(data[DATABASE['table']['audit']['name']])
        id = self.collection.insert_one(audit)
        return id.inserted_id