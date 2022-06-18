from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class FindByIdControlAuditRepository - Repositorio Control Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdControlAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    # @Overrride
    # @Method - Consulta un control de auditorias por el pk
    # @Parameter - data - {id} - Representa el pk
    # @Return - Collection
    def execute(self, data:dict):
        self.pk = DATABASE['table']['control_audit']['pk']
        self.id = DATABASE['table']['control_audit']['column'][0]
        return self.collection.find_one({
            self.pk:ObjectId(data[self.id])
        })
       