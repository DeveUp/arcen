from fastapi import FastAPI

# ROUTES DOCUMENT
from src.route.document.FindAllDocumentRouter import router_find_all_document
from src.route.document.FindByIdDocumentRouter import router_find_by_id_document
from src.route.document.SaveDocumentRouter import router_save_document


routes = FastAPI()

# ADD ROUTES
routes.include_router(router_find_all_document)
routes.include_router(router_find_by_id_document)
routes.include_router(router_save_document)