def auditSerializer(audit) -> dict:
    return {
        "id": str(audit["_id"]),
        "service": audit["servicio"],
        "operation": audit["operacion"],
        "idUser": audit["idUsuario"],
        "response": audit["respuesta"],
        "date": audit["fechaCreacion"]
    }

def auditsSerializer(audits) -> list:
    return [auditSerializer(audit) for audit in audits]