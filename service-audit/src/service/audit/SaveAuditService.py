from src.service.IService import IService
from src.persistence.repository.audit.SaveAuditRepository import SaveAuditRepository

class SaveAuditService(IService):

    def __init__(self):
        self.repository = SaveAuditRepository()

    def execute(self, data):
        element = self.repository.execute(data)
        return element