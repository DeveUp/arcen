"""
    @name - Routes
    @description - Puntos de entradas del microservicio box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
import imp
from fastapi import FastAPI


# ROUTES ROLE
from src.route.Role.DeleteByIdRoleRouter import router_detele_by_id_role
from src.route.Role.FindAllRoleRouter import router_find_all_role
from src.route.Role.SaveRoleRouter import router_save_role
from src.route.Role.FindByIdRoleRouter import router_find_by_id_role
from src.route.Role.UpdateRoleRouter import router_update_role


# ROUTES USER
from src.route.User.DeleteByIdUserRouter import router_detele_by_id_user
from src.route.User.FindAllUserRouter import router_find_all_user
from src.route.User.FindByIdUserRouter import router_find_by_id_user
from src.route.User.SaveUserRouter import router_save_user
from src.route.User.UpdateUserRouter import router_update_user


# ROUTES USER ROLE
from src.route.UserRole.FindAllUserRoleRouter import router_find_all_user_role
from src.route.UserRole.FindByIdUserRoleRouter import router_find_by_id_user_role
from src.route.UserRole.SaveUserRoleRouter import router_save_user_role
from src.route.UserRole.DeleteByIdUserRoleRouter import router_detele_by_id_user_role
from src.route.UserRole.UpdateUserRoleRouter import router_update_user_role

from src.route.Login.LoginUserRouter import router_login_user
from src.route.Login.LogoutUserRouter import router_logout_user

routes = FastAPI()

# ADD ROUTES

"""
    @description - Puntos de entradas servicio role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_role)
routes.include_router(router_find_all_role)
routes.include_router(router_save_role)
routes.include_router(router_find_by_id_role)
routes.include_router(router_update_role)

"""
    @description - Puntos de entradas servicio user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_user)
routes.include_router(router_find_all_user)
routes.include_router(router_find_by_id_user)
routes.include_router(router_save_user)
routes.include_router(router_update_user)

"""
    @description - Puntos de entradas servicio user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
routes.include_router(router_detele_by_id_user_role)
routes.include_router(router_find_all_user_role)
routes.include_router(router_find_by_id_user_role)
routes.include_router(router_save_user_role)
routes.include_router(router_update_user_role)

routes.include_router(router_login_user)
routes.include_router(router_logout_user)