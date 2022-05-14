from fastapi import APIRouter

from src.service.audit.DeleteByIdAuditService import DeleteByIdAuditService

router_detele_by_id_audit = APIRouter()

@router_detele_by_id_audit.delete("/{id}")
async def delete_by_id(id: str):
    data = dict(id=id);
    return DeleteByIdAuditService.execute(data)