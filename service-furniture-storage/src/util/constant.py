# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_BLOCK = "/block"
ENDPOINT_APP_FURNITURE = "/furniture"
ENDPOINT_APP_TYPE_FURNITURE = "/type-furniture"

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
DATABASE_POSTGRESQL_DATABASE = "arcen_furniture";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://{0}:{1}@{2}{3}/{4}".format(
    DATABASE_POSTGRESQL_USER,
    DATABASE_POSTGRESQL_PASSWORD,
    DATABASE_POSTGRESQL_HOST,
    DATABASE_POSTGRESQL_PORT,
    DATABASE_POSTGRESQL_DATABASE
)

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_BLOCK = "block"
DATABASE_POSTGRESQL_TABLE_FURNITURE = "furniture"
DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE = "type_furniture"

# COLUMNA BLOCK
COLUMN_BLOCK = "block"
COLUMN_BLOCK_ID = "id"
COLUMN_BLOCK_LETTER = "letter"
COLUMN_BLOCK_FLAT = "flat"
COLUMN_BLOCK_CREATION_DATE = "date"

# COLUMNA FURNITURE
COLUMN_FURNITURE = "furniture"
COLUMN_FURNITURE_ID = "id"
COLUMN_FURNITURE_ID_BLOCK = "id_block"
COLUMN_FURNITURE_ID_TYPE_FURNITURE = "id_type_furniture"
COLUMN_FURNITURE_NUMBER_FURNITURE = "number_furniture"
COLUMN_FURNITURE_CREATION_DATE = "date"

# COLUMNA TYPE FURNITURE
COLUMN_TYPE_FURNITURE = "type_furniture"
COLUMN_TYPE_FURNITURE_ID = "id"
COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE = "number_type_furniture"
COLUMN_TYPE_FURNITURE_COUNT_RACK = "count_rack"
COLUMN_TYPE_FURNITURE_COUNT_ROW = "count_row"
COLUMN_TYPE_FURNITURE_DEPTH = "depth"
COLUMN_TYPE_FURNITURE_HEIGHT = "height"
COLUMN_TYPE_FURNITURE_WIDTH= "width"
COLUMN_TYPE_FURNITURE_CREATION_DATE = "date"

# FEIGN
FEIGN_TYPE_POST = "POST"
FEIGN_TYPE_GET = "GET"
FEIGN_TYPE_PUT = "PUT"
FEIGN_TYPE_DELETE = "DELETE"

FEIGN_ENDPOINT = "endpoint"
FEIGN_ENDPOINT_AUDIT = "http://127.0.0.1:82/api/audit"
FEIGN_ENDPOINT_AUDIT_SAVE = "/"

# RESPONSE STATUS
RESPONSE_STATUS_CODE_GET = 200
RESPONSE_STATUS_CODE_POST = 201
RESPONSE_STATUS_CODE_PUT = 202
RESPONSE_STATUS_CODE_DELETE = 204

RESPONSE_STATUS_CODE_GENERIC_FIND_ALL = RESPONSE_STATUS_CODE_GET
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID = RESPONSE_STATUS_CODE_GET
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT = 424
RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID = RESPONSE_STATUS_CODE_DELETE
RESPONSE_STATUS_CODE_GENERIC_DELETE_BY_ID_NOT_CONTENT = 418
RESPONSE_STATUS_CODE_GENERIC_SAVE = RESPONSE_STATUS_CODE_POST
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE = 423
RESPONSE_STATUS_CODE_GENERIC_UPDATE = RESPONSE_STATUS_CODE_PUT
RESPONSE_STATUS_CODE_GENERIC_UPDATE_NOT_CONTENT = 424

RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE = 423

# RESPONSE MODEL
RESPONSE_MODEL_BLOCK_FIND_ALL = list
RESPONSE_MODEL_BLOCK_DELETE_BY_ID = bool

RESPONSE_MODEL_FURNITURE_FIND_ALL = list
RESPONSE_MODEL_FURNITURE_DELETE_BY_ID = bool

RESPONSE_MODEL_TYPE_FURNITURE_FIND_ALL = list
RESPONSE_MODEL_TYPE_FURNITURE_DELETE_BY_ID = bool

# RESPONSE MSG
RESPONSE_MSG_AUDIT_ERROR_SAVE = "Ups hemos tenido un problema interno! vuelva a intentar mas tarde."

RESPONSE_MSG_BLOCK_FIND_BY_ID_NOT_CONTENT =  "No nos cuadra el bloque suministrado, por favor verifica!."
RESPONSE_MSG_BLOCK_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el bloque, vuelva a intentar mas tarde."
RESPONSE_MSG_BLOCK_SAVE_ERROR_SAVE =  "No se registro el bloque... vuelva a intentar mas tarde."
RESPONSE_MSG_BLOCK_UPDATE_NOT_CONTENT = "No hemos podido actualizar el bloque. Vuelva a intentar mas tarde."

RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT =  "No nos cuadra el mueble suministrado, por favor verifica!."
RESPONSE_MSG_FURNITURE_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el mueble, vuelva a intentar mas tarde."
RESPONSE_MSG_FURNITURE_SAVE_ERROR_SAVE =  "No se registro el mueble... vuelva a intentar mas tarde."

RESPONSE_MSG_TYPE_FURNITURE_FIND_BY_ID_NOT_CONTENT =  "No nos cuadra el tipo de mueble suministrado, por favor verifica!."
RESPONSE_MSG_TYPE_FURNITURE_DELETE_BY_ID_NOT_CONTENT =  "No se logro eliminar el tipo de mueble, vuelva a intentar mas tarde."


# AUDIT
AUDIT_BLOCK_SERVICE = "BLOCK"
AUDIT_BLOCK_OPERATION_SAVE = "SAVE"
AUDIT_BLOCK_OPERATION_UPDATE = "UPDATE"
AUDIT_BLOCK_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"

AUDIT_FURNITURE_SERVICE = "FURNITURE"
AUDIT_FURNITURE_OPERATION_SAVE = "SAVE"
AUDIT_FURNITURE_OPERATION_UPDATE = "UPDATE"
AUDIT_FURNITURE_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"

AUDIT_TYPE_FURNITURE_SERVICE = "TYPE_FURNITURE"
AUDIT_TYPE_FURNITURE_OPERATION_SAVE = "SAVE"
AUDIT_TYPE_FURNITURE_OPERATION_UPDATE = "UPDATE"
AUDIT_TYPE_FURNITURE_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"

# DATA
DATA_REMOVE = "isRemove"
DATA_REMOVE_VALUE_DEFAULT = False