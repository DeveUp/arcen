from src.persistence.repository.IRepository import IRepository

from src.persistence.database.AuditDB import AuditDB

# @Class FindAllAuditRepository - Repositorio Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    # @Overrride
    # @Method - Consulta todas las auditorias
    # @Parameter - data (Optional) - No cumple
    # @Return - Collections
    def execute(self, data:dict):
        return self.collection.find()