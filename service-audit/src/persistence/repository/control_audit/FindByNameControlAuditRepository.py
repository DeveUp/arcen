from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class FindByNameControlAuditRepository - Repositorio Control Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByNameControlAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    # @Method - Consulta un control de auditorias por el nombre
    # @Parameter - data - {name} - Representa el nombre del control
    # @Return - Collection
    def execute(self, data:dict):
        self.name = DATABASE['table']['control_audit']['column'][1]
        return self.collection.find_one({
            self.name:data[self.name]
        })