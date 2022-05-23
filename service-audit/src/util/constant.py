# UVICORN
from tkinter import EXCEPTION


APP_UVICORN_NAME= "main:app"
APP_UVICORN_HOST = "http://127.0.0.1/"
APP_UVICORN_PORT = 5000
APP_UVICORN_LOG = "info"


# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_AUDIT = "/audit"
ENDPOINT_APP_AUDIT_CLOSURE = "/audit-closure"
ENDPOINT_APP_CONTROL_AUDIT_CLOSURE = "/control-audit-closure"
ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID = "/table-id/{table}"
ENDPOINT_GENERIC_FIND_BY_ID = "/{id}"
ENDPOINT_GENERIC_FIND_BY_RANGE_DATE = "/all/find/range/date/{start}/{end}"
ENDPOINT_GENERIC_FIND_ALL = "/"
ENDPOINT_GENERIC_SAVE = "/"

# DATABASE
DATABASE_MONGODB_USER = "arcen:arcen";
DATABASE_MONGODB_CLUSTER = "@cluster0.qahfe.mongodb.net";
DATABASE_MONGODB_URL = "mongodb+srv://"+DATABASE_MONGODB_USER+DATABASE_MONGODB_CLUSTER+"/test";
DATABASE_MONGODB_NAME = "arcen_audit";
DATABASE_MONGODB_NAME_TABLE = "audit";
DATABASE_MONGODB = DATABASE_MONGODB_URL +DATABASE_MONGODB_NAME;

# COLUMNA TABLE AUDIT
COLUMN_AUDIT_CLOSURE_NAME = "audit-closure"
COLUMN_AUDIT_CLOSURE_DATE_START_NAME = "date_start"
COLUMN_AUDIT_CLOSURE_DATE_END_NAME = "date_end"

# COLUMNA TABLE AUDIT
COLUMN_AUDIT_NAME = "audit"
COLUMN_AUDIT_ID_NAME = "_id"
COLUMN_AUDIT_ID_TWO_NAME = "id"
COLUMN_AUDIT_SERVICE_NAME = "service"
COLUMN_AUDIT_OPERATION_NAME = "operation"
COLUMN_AUDIT_ID_USER_NAME = "id_user"
COLUMN_AUDIT_RESPONSE_NAME = "response"
COLUMN_AUDIT_DATE_NAME = "date"
COLUMN_AUDIT_DATE_START_NAME = "start"
COLUMN_AUDIT_DATE_END_NAME = "end"

# COLUMNA TABLE CONTROL AUDIT
COLUMN_CONTROL_AUDIT_NAME = "control_audit"
COLUMN_CONTROL_AUDIT_ID_NAME = "_id"
COLUMN_CONTROL_AUDIT_ID_TWO_NAME = "id"
COLUMN_CONTROL_AUDIT_NAME_NAME = "name"
COLUMN_CONTROL_AUDIT_DATE_START_NAME = "date_start"
COLUMN_CONTROL_AUDIT_DATE_END_NAME = "date_end"
COLUMN_CONTROL_AUDIT_DATE_NAME = "date"

# FORMAT
FORMAT_DATE = '%Y-%m-%d %H:%M'
FORMAT_DATE_STR = '%Y-%m-%d'

# EXCEPTION
EXCEPTION_MSG_GENERIC_DATE_START_FORMAT = "El formato de la fecha de inicio no es valido."
EXCEPTION_MSG_GENERIC_DATE_END_FORMAT = "El formato de la fecha de fin no es valido."

EXCEPTION_MSG_AUDIT_FIND_ALL = "No se encontro ninguna auditoria."