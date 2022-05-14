from src.service.IService import IService
from src.persistence.repository.audit.UpdateAuditRepository import UpdateAuditRepository

class UpdateAuditService(IService):

    def __init__(self):
        self.repository = UpdateAuditRepository()

    def execute(self, data):
        element = self.repository.execute(data)
        return element