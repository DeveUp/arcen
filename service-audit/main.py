from fastapi import FastAPI

from src.route.AuditRouter import audit_router

app = FastAPI()

app.include_router(audit_router)