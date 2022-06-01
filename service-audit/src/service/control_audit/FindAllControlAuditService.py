from src.service.IService import IService
from src.persistence.repository.control_audit.FindAllControlAuditRepository import FindAllControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

class FindAllControlAuditService(IService):

    def __init__(self):
        self.repository = FindAllControlAuditRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)