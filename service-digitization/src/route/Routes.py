"""
    @description - Puntos de entradas del microservicio digitalizacion
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import FastAPI

# ROUTES DOCUMENT
from src.route.document.FindAllDocumentRouter import router_find_all_document
# from src.route.document.FindByIdDocumentRouter import router_find_by_id_document
from src.route.document.SaveDocumentRouter import router_save_document

# ROUTES DOCUMENT LOCATION
# from src.route.document_location.FindAllDocumentLocationRouter import router_find_all_document_location
# from src.route.document_location.FindByIdDocumentLocationRouter import router_find_by_id_document_location
# from src.route.document_location.SaveDocumentLocationRouter import router_save_document_location

# ROUTES DOCUMENT VERSION
# from src.route.document_version.FindAllDocumentVersionRouter import router_find_all_document_version
# from src.route.document_version.FindByIdDocumentVersionRouter import router_find_by_id_document_version
# from src.route.document_version.SaveDocumentVersionRouter import router_save_document_version

routes = FastAPI()

"""
    @description - Puntos de entradas servicio documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
routes.include_router(router_find_all_document)
# routes.include_router(router_find_by_id_document)
routes.include_router(router_save_document)

"""
    @description - Puntos de entradas servicio ubicacion del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
# routes.include_router(router_find_all_document_location)
# routes.include_router(router_find_by_id_document_location)
# routes.include_router(router_save_document_location)

"""
    @description - Puntos de entradas servicio version del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
# routes.include_router(router_find_all_document_version)
# routes.include_router(router_find_by_id_document_version)
# routes.include_router(router_save_document_version)