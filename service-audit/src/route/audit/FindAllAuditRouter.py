from fastapi import APIRouter

from src.service.audit.FindByIdAuditService import FindByIdAuditService

router_find_all_audit = APIRouter()

@router_find_all_audit.get("/")
async def find_all():
    data = dict()
    return FindByIdAuditService.execute(data)