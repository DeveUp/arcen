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

routes = FastAPI()

# ADD ROUTES
routes.include_router(router_detele_by_id_role)
routes.include_router(router_find_all_role)
routes.include_router(router_save_role)
routes.include_router(router_find_by_id_role)
routes.include_router(router_update_role)

routes.include_router(router_detele_by_id_user)
routes.include_router(router_find_all_user)
routes.include_router(router_find_by_id_user)
routes.include_router(router_save_user)
routes.include_router(router_update_user)



routes.include_router(router_find_all_user_role)
routes.include_router(router_find_by_id_user_role)
routes.include_router(router_save_user_role)