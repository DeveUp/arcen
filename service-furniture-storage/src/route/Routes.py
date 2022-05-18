from fastapi import FastAPI

# ROUTES BLOCK
from src.route.block.DeleteByIdBlockRouter import router_detele_by_id_block
from src.route.block.FindAllBlockRouter import router_find_all_block
from src.route.block.FindByIdBlockRouter import router_find_by_id_block
from src.route.block.SaveBlockRouter import router_save_block
from src.route.block.UpdateBlockRouter import router_update_block

# ROUTES FURNITURE
from src.route.furniture.DeleteByIdFurnitureRouter import router_detele_by_id_furniture
from src.route.furniture.FindAllFurnitureRouter import router_find_all_furniture
from src.route.furniture.FindByIdFurnitureRouter import router_find_by_id_furniture
from src.route.furniture.SaveFurnitureRouter import router_save_furniture
from src.route.furniture.UpdateFurnitureRouter import router_update_furniture

# ROUTES TYPE FURNITURE
# from src.route.type_furniture.DeleteByIdTypeFurnitureRouter import router_detele_by_id_type_furniture
# from src.route.type_furniture.FindAllTypeFurnitureRouter import router_find_all_type_furniture
# from src.route.type_furniture.FindByIdTypeFurnitureRouter import router_find_by_id_type_furniture
# from src.route.type_furniture.SaveTypeFurnitureRouter import router_save_type_furniture
# from src.route.type_furniture.UpdateTypeFurnitureRouter import router_update_type_furniture

routes = FastAPI()

# ADD ROUTES
routes.include_router(router_detele_by_id_block)
routes.include_router(router_find_all_block)
routes.include_router(router_find_by_id_block)
routes.include_router(router_save_block)
routes.include_router(router_update_block)

routes.include_router(router_detele_by_id_furniture)
routes.include_router(router_find_all_furniture)
routes.include_router(router_find_by_id_furniture)
routes.include_router(router_save_furniture)
routes.include_router(router_update_furniture)

# routes.include_router(router_detele_by_id_type_furniture)
# routes.include_router(router_find_all_type_furniture)
# routes.include_router(router_find_by_id_type_furniture)
# routes.include_router(router_save_type_furniture)
# routes.include_router(router_update_type_furniture)