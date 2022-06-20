"""
    @name - Routes
    @description - Puntos de entradas del microservicio objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import FastAPI

# ROUTES TYPE OBJECT
from src.route.type_object.DeleteByIdTypeObjectRouter import router_detele_by_id_type_object
from src.route.type_object.FindAllTypeObjectRouter import router_find_all_type_object
from src.route.type_object.FindByIdTypeObjectRouter import router_find_by_id_type_object
from src.route.type_object.SaveTypeObjectRouter import router_save_type_object
from src.route.type_object.UpdateTypeObjectRouter import router_update_type_object

# ROUTES SUBOBJECT
from src.route.subobject.DeleteByIdSubObjectRouter import router_detele_by_id_subobject
from src.route.subobject.FindAllSubObjectRouter import router_find_all_subobject
from src.route.subobject.FindByIdSubObjectRouter import router_find_by_id_subobject
from src.route.subobject.SaveSubObjectRouter import router_save_subobject
from src.route.subobject.UpdateSubObjectRouter import router_update_subobject

# ROUTES OBJECT
from src.route.object.DeleteByIdObjectRouter import router_detele_by_id_object
from src.route.object.FindAllObjectRouter import router_find_all_object
from src.route.object.FindByIdObjectRouter import router_find_by_id_object
from src.route.object.SaveObjectRouter import router_save_object
from src.route.object.UpdateObjectRouter import router_update_object

routes = FastAPI()

"""
    @description - Puntos de entradas servicio tipo de objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
routes.include_router(router_detele_by_id_type_object)
routes.include_router(router_find_all_type_object)
routes.include_router(router_find_by_id_type_object)
routes.include_router(router_save_type_object)
routes.include_router(router_update_type_object)

"""
    @description - Puntos de entradas servicio subobjecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
routes.include_router(router_detele_by_id_subobject)
routes.include_router(router_find_all_subobject)
routes.include_router(router_find_by_id_subobject)
routes.include_router(router_save_subobject)
routes.include_router(router_update_subobject)

"""
    @description - Puntos de entradas servicio objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
routes.include_router(router_detele_by_id_object)
routes.include_router(router_find_all_object)
routes.include_router(router_find_by_id_object)
routes.include_router(router_save_object)
routes.include_router(router_update_object)