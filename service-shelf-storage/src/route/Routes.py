from fastapi import FastAPI


# ROUTES TYPE SHELF
from src.route.Type_Shelf.DeleteByIdTypeShelfRouter import router_detele_by_id_type_shelf
from src.route.Type_Shelf.FindAllTypeShelfRouter import router_find_all_type_shelf
from src.route.Type_Shelf.FindByIdTypeShelfRouter import router_find_by_id_type_shelf
from src.route.Type_Shelf.SaveTypeShelfRouter import router_save_type_shelf
#from src.route.Type_Shelf.UpdateTypeShelfRouter import router_update_type_shelf

routes = FastAPI()
# ADD ROUTES


routes.include_router(router_detele_by_id_type_shelf)
routes.include_router(router_find_all_type_shelf)
routes.include_router(router_find_by_id_type_shelf)
routes.include_router(router_save_type_shelf)
#routes.include_router(router_update_type_shelf)