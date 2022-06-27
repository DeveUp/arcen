"""
    @name - AuditDto
    @description - Dto auditoria
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel

class AuditDto(BaseModel):
    service: str
    operation: str
    id_user: str
    response: str