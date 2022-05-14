from fastapi import APIRouter

from src.service.audit.FindAllAuditService import FindAllAuditService

router_find_all_audit = APIRouter()

@router_find_all_audit.get("/")
async def find_all():
    service = FindAllAuditService()
    return service.execute(dict())