from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class SaveControlAuditRepository - Repositorio Control Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveControlAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    # @Overrride
    # @Method - Regustra un control de auditoria
    # @Parameter - data - {control_audit} - Representa el control de auditoria
    # @Return - PK
    def execute(self, data:dict):
        control_audit = dict(data[DATABASE['table']['control_audit']['name']])
        id = self.collection.insert_one(control_audit)
        return id.inserted_id