from src.model.entity.Audit import Audit

class AuditSchema:

    def __init__(self):
        self.id = "_id"
        self.service = "servicio"
        self.operation = "operacion"
        self.id_user = "id_usuario"
        self.response = "respuesta"
        self.date = "fecha_creacion"

    def audit(self, audit) -> Audit:
        id = str(audit[self.id])
        service = audit[self.service]
        operation = audit[self.operation]
        id_user = audit[self.id_user]
        response = audit[self.response]
        date = audit[self.date]
        return Audit(id,service,operation,id_user,response,date)

    def audit_dic(self,audit) -> dict:
        return {
            "id": str(audit[self.id]),
            "service": audit[self.service],
            "operation": audit[self.operation],
            "idUser": audit[self.id_user],
            "response": audit[self.response],
            "date": audit[self.date]
        }
    
    def audits(self, audits) -> list:
        return [self.audit(self, audit) for audit in audits]

    def audits_dic(self, audits) -> list:
        return [self.audit_dic(self, audit) for audit in audits]