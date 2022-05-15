from fastapi import FastAPI

# ROUTES AUDIT
from src.route.audit.DeleteByIdAuditRouter import router_detele_by_id_audit
from src.route.audit.FindAllAuditRouter import router_find_all_audit
from src.route.audit.FindByIdAuditRouter import router_find_by_id_audit
from src.route.audit.SaveAuditRouter import router_save_audit
from src.route.audit.UpdateAuditRouter import router_update_audit

routes = FastAPI()

# ADD ROUTES
routes.include_router(router_detele_by_id_audit)
routes.include_router(router_find_all_audit)
routes.include_router(router_find_by_id_audit)
routes.include_router(router_save_audit)
routes.include_router(router_update_audit)