# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_ROLE = "/role"
ENDPOINT_APP_USER = "/user"
ENDPOINT_APP_USER_ROLE = "/user-role"
ENDPOINT_APP_LOGIN = "/login"
ENDPOINT_APP_LOGOUT = "/logout"

ENDPOINT_GENERIC_FIND_BY_ID = "/{id}"
ENDPOINT_GENERIC_FIND_ALL = "/"
ENDPOINT_GENERIC_SAVE = "/"
ENDPOINT_GENERIC_UPDATE= "/{id}"
ENDPOINT_GENERIC_DELETE_BY_ID = "/{id}"

# DATABASE VARS
DATABASE_POSTGRESQL_USER = "arcen";
DATABASE_POSTGRESQL_PASSWORD = "arcen";
DATABASE_POSTGRESQL_HOST = "localhost";
DATABASE_POSTGRESQL_PORT = "";
DATABASE_POSTGRESQL_DATABASE = "arcen_user";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://arcen:arcen@arcen-postgresql:5432/arcen"

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_ROLE = "role"
DATABASE_POSTGRESQL_TABLE_USER = "user"
DATABASE_POSTGRESQL_TABLE_USER_ROLE = "user_role"


# COLUMNA ROLE
COLUMN_ROLE = "role"
COLUMN_ROLE_ID = "id"
COLUMN_ROLE_NAME = "name"
COLUMN_ROLE_DATE = "date"

# COLUMNA USER  
COLUMN_USER = "user"
COLUMN_USER_ID = "id"
COLUMN_USER_DOCUMENT = "document"
COLUMN_USER_FULL_NAME = "full_name"
COLUMN_USER_PASSWORD = "password"
COLUMN_USER_EMAIL = "email"
COLUMN_USER_STATUS = "status"
COLUMN_USER_DATE = "date"
COLUMN_USER_SESSION_STARTED = "session_started"

# COLUMNA USER_ROLE
COLUMN_USER_ROLE = "user_role"
COLUMN_USER_ROLE_ID = "id"
COLUMN_USER_ROLE_ID_ROLE = "id_role"
COLUMN_USER_ROLE_ID_USER = "id_user"
COLUMN_USER_ROLE_ID_DEPENDENCE = "id_dependence"
COLUMN_USER_ROLE_DATE_CREATION = "date_creation"
COLUMN_USER_ROLE_DATE_END = "date_end"
COLUMN_USER_ROLE_STATUS = "status"

# FEIGN
FEIGN_TYPE_POST = "POST"
FEIGN_TYPE_GET = "GET"
FEIGN_TYPE_PUT = "PUT"
FEIGN_TYPE_DELETE = "DELETE"

FEIGN_ENDPOINT = "endpoint"
FEIGN_ENDPOINT_AUDIT = "http://arcen-service-audit:8001/api/audit"
FEIGN_ENDPOINT_AUDIT_SAVE = "/"

FEIGN_ENDPOINT_DEPENDENCE = "http://arcen-service-shelf-storage:8008/api/dependence"
FEIGN_ENDPOINT_DEPENDENCE_SAVE = "/"

# RESPONSE STATUS
RESPONSE_STATUS_CODE_GET = 200
RESPONSE_STATUS_CODE_POST = 201
RESPONSE_STATUS_CODE_PUT = 202
RESPONSE_STATUS_CODE_DELETE = 204

# RESPONSE MODEL
RESPONSE_MODEL_FIND_ALL_GENERIC = list
RESPONSE_MODEL_DELETE_BY_ID_GENERIC = bool



# RESPONSE STATUS
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL = 200
RESPONSE_STATUS_CODE_GENERIC_LOGIN = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT = 400
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT = 424
RESPONSE_STATUS_CODE_GENERIC_SAVE = 201
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE = 423
RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID = 204
RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT = 418
RESPONSE_STATUS_CODE_GENERIC_UPDATE = 202

RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE = 423

# RESPONSE MODEL
RESPONSE_MODEL_GENERIC_FIND_ALL = list

# RESPONSE MSG
RESPONSE_MSG_AUDIT_ERROR_SAVE = "Ups hemos tenido un problema interno! vuelva a intentar mas tarde."
RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT = "Por favor verificar las fechas no son validas."

RESPONSE_MSG_ROLE_FIND_BY_ID_NOT_CONTENT =  "No se encontro un rol con el id suministrado."
RESPONSE_MSG_ROLE_SAVE_ERROR_SAVE =  "No se registro el rol.. vuelvalo a intentar mas tarde."
RESPONSE_MSG_ROLE_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el rol, vuelva a intentar mas tarde."

RESPONSE_MSG_USER_FIND_BY_ID_NOT_CONTENT =  "No se encontro un usuario con el id suministrado."
RESPONSE_MSG_USER_SAVE_ERROR_SAVE =  "No se registro el usuario.. vuelvalo a intentar mas tarde."
RESPONSE_MSG_USER_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el usuario, vuelva a intentar mas tarde."

RESPONSE_MSG_USER_ROLE_FIND_BY_ID_NOT_CONTENT =  "No se encontro un rol del usuario con el id suministrado."
RESPONSE_MSG_USER_ROLE_SAVE_ERROR_SAVE =  "No se registro el rol del usuario.. vuelvalo a intentar mas tarde."
RESPONSE_MSG_USER_ROLE_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el rol del usuario, vuelva a intentar mas tarde."

RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT = "No se encontro ningun dependencia con el id suministrado."

RESPONSE_MSG_USER_LOGIN_ERROR = "Usuario: Documento,Correo o la Clave son invalidos"

RESPONSE_MSG_USER_LOGOUT_ERROR = "Error, El usuario no esta logueado en el sistema"

# AUDIT
AUDIT_USER_SERVICE = "USER"
AUDIT_ROLE_SERVICE = "ROLE"
AUDIT_USER_ROLE_SERVICE = "USER_ROLE"

AUDIT_GENERIC_OPERATION_SAVE = "SAVE"
AUDIT_GENERIC_OPERATION_UPDATE = "UPDATE"
AUDIT_GENERIC_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"

# DATA
DATA_REMOVE = "isRemove"
DATA_REMOVE_VALUE_DEFAULT = False

DEPENDENCE_SERVICE_HOST_URL = 'http://localhost:8004/api/dependence/'