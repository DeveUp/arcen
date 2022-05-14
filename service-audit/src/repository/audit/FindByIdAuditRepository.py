from src.repository.IRepository import IRepository

from src.util.database import COLLECTION_AUDIT

class FindByIdAuditRepository(IRepository):

    def execute(self, data:dict):
        return ""