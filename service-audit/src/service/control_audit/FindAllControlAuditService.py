from src.service.IService import IService
from src.persistence.repository.control_audit.FindAllControlAuditClosureRepository import FindAllControlAuditClosureRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

class FindAllControlAuditService(IService):

    def __init__(self):
        self.repository = FindAllControlAuditClosureRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)