from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class SaveAuditClosureRepository - Repositorio Cierre Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveAuditClosureRepository(IRepository):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el id de la tabla
    # @Return - Void
    def __init__(self, table_id: str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    # @Overrride
    # @Method - Registra un cierre de auditoria
    # @Parameter - data - {closure_audit} - Representa el cierre de auditoria
    # @Return - PK
    def execute(self, data:dict):
        closure_audit = dict(data[DATABASE['table']['audit_closure']['subname']])
        id = self.collection.insert_one(closure_audit)
        return id.inserted_id