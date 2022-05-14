from src.persistence.repository.IRepository import IRepository

from src.persistence.database.AuditDB import AuditDB

class UpdateAuditRepository(IRepository):

    def execute(self, data:dict):
        return ""