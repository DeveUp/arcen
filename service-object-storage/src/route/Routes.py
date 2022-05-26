from fastapi import FastAPI

# ROUTES OBJECT
from src.route.object.DeleteByIdObjectRouter import router_detele_by_id_arcen
from src.route.object.FindAllObjectRouter import router_find_all_object
from src.route.object.FindByIdObjectRouter import router_find_by_id_object
from src.route.object.SaveObjectRouter import router_save_object
from src.route.object.UpdateObjectRouter import router_update_object

routes = FastAPI()

# ADD ROUTES
routes.include_router(router_detele_by_id_arcen)
routes.include_router(router_find_all_object)
routes.include_router(router_find_by_id_object)
routes.include_router(router_save_object)
routes.include_router(router_update_object)