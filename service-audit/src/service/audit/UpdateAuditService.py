from src.service.IService import IService
from src.persistence.repository.audit.UpdateAuditRepository import UpdateAuditRepository

class UpdateAuditService(IService):

    def __init__(self):
        self.repository = UpdateAuditRepository()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
        except:
            element= None
        return element