from src.service.IService import IService
from src.persistence.repository.control_audit.FindAllControlAuditClosureRepository import FindAllControlAuditClosureRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

class FindAllControlAuditService(IService):

    def __init__(self):
        self.repository = FindAllControlAuditClosureRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements