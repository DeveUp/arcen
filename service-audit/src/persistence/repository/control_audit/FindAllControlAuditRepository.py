from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

# @Class FindAllControlAuditRepository - Repositorio Control Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllControlAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    # @Overrride
    # @Method - Consulta los control de auditorias
    # @Parameter - data (Optional) - No cumple
    # @Return - Collections
    def execute(self, data:dict):
        return self.collection.find()