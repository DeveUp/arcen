from fastapi import APIRouter

from src.service.audit.FindByIdAuditService import FindByIdAuditService

router_find_by_id_audit = APIRouter()

@router_find_by_id_audit.get("/{id}")
async def find_by_id(id: str):
    data = dict(id=id)
    service = FindByIdAuditService()
    return service.execute(data)