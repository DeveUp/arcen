"""
    @name - Routes
    @description - Puntos de entradas del microservicio shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import FastAPI

# ROUTES DEPENDENCE
from src.route.dependece.DeleteByIdDependenceRouter import router_detele_by_id_dependence
from src.route.dependece.FindAllDependenceRouter import router_find_all_dependence
from src.route.dependece.FindByIdDependenceRouter import router_find_by_id_dependence
from src.route.dependece.SaveDependenceRouter import router_save_dependence
from src.route.dependece.UpdateDependenceRouter import router_update_dependence


# ROUTES TYPE SHELF
from src.route.Type_Shelf.DeleteByIdTypeShelfRouter import router_detele_by_id_type_shelf
from src.route.Type_Shelf.FindAllTypeShelfRouter import router_find_all_type_shelf
from src.route.Type_Shelf.FindByIdTypeShelfRouter import router_find_by_id_type_shelf
from src.route.Type_Shelf.SaveTypeShelfRouter import router_save_type_shelf
from src.route.Type_Shelf.UpdateTypeShelfRouter import router_update_type_shelf

# ROUTES  SHELF
from src.route.shelf.DeleteByIdShelfRouter import router_detele_by_id_shelf
from src.route.shelf.FindAllShelfRouter import router_find_all_shelf
from src.route.shelf.FindByIdShelfRouter import router_find_by_id_shelf
from src.route.shelf.SaveShelfRouter import router_save_shelf
from src.route.shelf.UpdateShelfRouter import router_update_shelf

routes = FastAPI()
# ADD ROUTES

"""
    @description - Puntos de entradas servicio type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_type_shelf)
routes.include_router(router_find_all_type_shelf)
routes.include_router(router_find_by_id_type_shelf)
routes.include_router(router_save_type_shelf)
routes.include_router(router_update_type_shelf)

"""
    @description - Puntos de entradas servicio dependence
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_dependence)
routes.include_router(router_find_all_dependence)
routes.include_router(router_find_by_id_dependence)
routes.include_router(router_save_dependence)
routes.include_router(router_update_dependence)

"""
    @description - Puntos de entradas servicio shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_shelf)
routes.include_router(router_find_all_shelf)
routes.include_router(router_find_by_id_shelf)
routes.include_router(router_save_shelf)
routes.include_router(router_update_shelf)