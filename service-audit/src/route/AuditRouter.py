from fastapi import APIRouter

from src.service.AuditService import findById, findAll, save, update, deleteById
from src.model.Audit import Audit

audit_router = APIRouter()

# GET - Find By Id
@audit_router.get("/{id}")
async def findByIdRouter(id: str):
    return findById(id)

# GET - Find All
@audit_router.get("/")
async def findAllRouter():
    return findAll

# POST - Create
@audit_router.post("/")
async def saveRouter(audit: Audit):
    return save(audit)

# PUT - Update
@audit_router.put("/{id}")
async def updateRouter(id: str, audit: Audit):
    return update(id, audit)

# DELETE - Delete By Id
@audit_router.delete("/{id}")
async def deleteByIdRouter(id: str):
    return deleteById(id)