from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

# @Class FindAllAuditClosureRepository - Repositorio Cierre Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllAuditClosureRepository(IRepository):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el id de la tabla
    # @Return - Void
    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    # @Method - Consulta todas los cierres de auditoria
    # @Parameter - data (Optional) - No cumple
    # @Return - Collections
    def execute(self, data:dict):
        return self.collection.find()