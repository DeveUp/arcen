from src.model.entity.Audit import Audit

class ClosureAudit():

    def __init__(self):
        self.id:str = None
        self.control:str = None
        self.audit:Audit = Audit()
        self.date:str = None
    
    def get_id(self) -> str:
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_control(self) -> str:
        return self.control
 
    def set_control(self, control):
        self.control = control
    
    def get_audit(self) -> Audit:
        return self.audit
    
    def set_audit(self, audit):
        self.audit = audit
    
    def get_date(self) -> str:
        return self.date
    
    def set_date(self, date):
        self.date = date