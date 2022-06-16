# FORMAT
FORMAT_DATE = '%Y-%m-%d %H:%M'
FORMAT_DATE_STR = '%Y-%m-%d'

# ENDPOINT
ENDPOINT = {
    "path": "/api",
    "service": {
        "audit": {
           "path": "/audit",
        },
        "audit_closure": {
            "path": "/audit-closure",
            "operation":{
                "get": {
                    "find_table_by_id": "/table-id/{table}"
                }
            }
        },
        "audit_control": {
           "path": "/audit-control" 
        }
    },
    "operation":{
        "get":{
            "find_by_id": "/{id}",
            "find_by_name": "/find-by-name/{name}",
            "find_all": "/",
            "find_by_range_date_all":  "/all/find/range/date/{start}/{end}"
        },
        "post":{
            "save": "/"
        }
    }
}

DATABASE= {
    "table":{
        "audit":{
            "name": "audit",
            "pk": "_id",
            "column": [
                "id",
                "service",
                "operation",
                "id_user",
                "ip_address",
                "response",
                "date",
                ["start", "end"]
            ]
        },
        "control_audit":{
            "name": "control-audit",
            "pk": "_id",
            "column": [
                "id",
                "name",
                "date_start",
                "date_end",
                "date"
            ]
        },
        "audit_closure":{
            "name": "audit-closure-%s",
            "pk": "_id",
            "column": [
                "id",
                "control",
                "audit",
                "date_start",
                "date_end",
                "date"
            ]
        }
    }
}


# RESPONSE STATUS
RESPONSE_GENERIC_CODE = {
    "success": {
        "find": 200,
        "save": 201,
        "update": 202,
        "delete": 204
    },
    "error": {
        "format": 422,
        "delete": 418,
        "save": 423,
        "find": 424,
        "update": 425,
        "request": 426,
        "persistence": 427
    }
}
RESPONSE_GENERIC = {
    "get":{
        "find_by_id":{
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['find']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['find'],
                    "msg": "¡Ups! verifique el id %s, no encontramos ningun resultado."
                }
            }
        },
        "find_by_name":{
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['find']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['find'],
                    "msg": "¡Ups! verifique el nombre %s, no encontramos ningun resultado."
                }
            }
        },
        "find_all":{
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['find']
                } 
            }
        },
        "find_by_range_date_all": {
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['find']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['format'],
                    "msg": "¡Ups! verifique las fechas no nos cuadra."
                }
            }
        }
    },
    "post": {
        "save": {
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['save']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['save'],
                    "msg": "Ouch! No pudismos registrar %s. Vuelva a intentar mas tarde!"
                }
            }
        }
    },
    "system": {
        "persistence": {
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['persistence'],
                    "msg": "No eres tu, somos nosotros. Hemos tenido un problema interno!"
                }
            }
        },
        "env": {
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['find'],
                    "msg": "Oh no! Lamentamos que no estemos para ti."
                }
            }
        }
    }
}

RESPONSE = {
    "audit":{
        "get": {
            "find_by_id":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_id']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_id']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("de la auditoria")
                    }
                }
            },
            "find_all":{
                "response": list,
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_all']['success']['default']['code']
                    }
                },
            }
        },  
        "post":{
            "save":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['success']['default']['code']
                    }
                }
            }
        }    
    },
    "audit_closure":{
        "get":{
            "find_by_id":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_id']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_id']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del cierre de auditoria")
                    }
                }
            },
        }
    }
}



RESPONSE_STATUS_CODE_GENERIC_SAVE = 201
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE = 423
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_NAME_SAVE = 426
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_RANGE_DATE_SAVE = 424
RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR = 427
RESPONSE_STATUS_CODE_GENERIC_ENV_ERROR = 424

# RESPONSE MODEL
RESPONSE_MODEL_AUDIT_FIND_ALL = list
RESPONSE_MODEL_AUDIT_FIND_ALL_BY_RANGE_DATE = list

RESPONSE_MODEL_CONTROL_AUDIT_FIND_ALL = list

RESPONSE_MODEL_CLOSURE_AUDIT_FIND_ALL = list
RESPONSE_MODEL_CLOSURE_AUDIT_SAVE = list


RESPONSE_MSG_AUDIT_FIND_BY_ID_NOT_CONTENT =  "No se encontro una auditoria con el id suministrado."
RESPONSE_MSG_AUDIT_SAVE_ERROR_SAVE =  "No se registro la auditoria, vuelvalo a intentar mas tarde."

RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_ID_NOT_CONTENT =  "No se encontro ningun control de auditoria con el id suministrado."
RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_NAME_NOT_CONTENT =  "No se encontro ningun control de auditoria con el nombre suministrado."
RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_SAVE =  "No se registro la auditoria, vuelvalo a intentar mas tarde."
RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_NAME_SAVE =  "Por favor verifica el nombre del control de auditoria, algo no nos cuadra!."
RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_RANGE_DATE_SAVE = "Por favor vuelva a intentar, no encontramos ninguna auditoria."

RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT = "No se encontro ningun control de auditoria con el id suministrado."
RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT =  "No se encontro ningun cierre de auditoria con el id suministrado."



#BORRAR
ENDPOINT_APP = "/api"
ENDPOINT_APP_AUDIT = "/audit"
ENDPOINT_APP_AUDIT_CLOSURE = "/audit-closure"
ENDPOINT_APP_CONTROL_AUDIT_CLOSURE = "/audit-control"
ENDPOINT_APP_AUDIT_CLOSURE_TABLE_ID = "/table-id/{table}"

ENDPOINT_GENERIC_FIND_BY_ID = "/{id}"
ENDPOINT_GENERIC_FIND_BY_NAME = "/find-by-name/{name}"
ENDPOINT_GENERIC_FIND_BY_RANGE_DATE = "/all/find/range/date/{start}/{end}"
ENDPOINT_GENERIC_FIND_ALL = "/"
ENDPOINT_GENERIC_SAVE = "/"

# DATABASE
DATABASE_MONGODB_USER = "arcen:arcen";
DATABASE_MONGODB_CLUSTER = "@cluster0.qahfe.mongodb.net";
DATABASE_MONGODB_URL = "mongodb+srv://"+DATABASE_MONGODB_USER+DATABASE_MONGODB_CLUSTER+"/";
DATABASE_MONGODB_DB = "arcen_audit";
DATABASE_MONGODB_TABLE = "audit";
DATABASE_MONGODB = DATABASE_MONGODB_URL +DATABASE_MONGODB_DB;

# COLUMNA TABLE AUDIT
COLUMN_AUDIT = "audit"
COLUMN_AUDIT_ID = "_id"
COLUMN_AUDIT_ID_TWO = "id"
COLUMN_AUDIT_SERVICE = "service"
COLUMN_AUDIT_OPERATION = "operation"
COLUMN_AUDIT_ID_USER = "id_user"
COLUMN_AUDIT_IP_ADDRESS = "ip_address"
COLUMN_AUDIT_RESPONSE = "response"
COLUMN_AUDIT_DATE = "date"
COLUMN_AUDIT_DATE_START = "start"
COLUMN_AUDIT_DATE_END = "end"

# COLUMNA TABLE CONTROL AUDIT
COLUMN_CONTROL_AUDIT = "control_audit"
COLUMN_CONTROL_AUDIT_ID = "_id"
COLUMN_CONTROL_AUDIT_ID_TWO = "id"
COLUMN_CONTROL_AUDIT_NAME = "name"
COLUMN_CONTROL_AUDIT_DATE_START = "date_start"
COLUMN_CONTROL_AUDIT_DATE_END = "date_end"
COLUMN_CONTROL_AUDIT_DATE = "date"

# COLUMNA TABLE AUDIT CLOSURE
COLUMN_AUDIT_CLOSURE = "audit-closure"
COLUMN_AUDIT_CLOSURE_ID = "_id"
COLUMN_AUDIT_CLOSURE_ID_TWO = "id"
COLUMN_AUDIT_CLOSURE_CONTROL = "control"
COLUMN_AUDIT_CLOSURE_AUDIT = "audit"
COLUMN_AUDIT_CLOSURE_DATE = "date"
COLUMN_AUDIT_CLOSURE_DATE_START = "date_start"
COLUMN_AUDIT_CLOSURE_DATE_END = "date_end"

RESPONSE_STATUS_CODE_GENERIC_FIND_ALL = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT = 400
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT = 424
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME= 200
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME_NOT_CONTENT = 424


# RESPONSE MSG
RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT = "Por favor verificar las fechas no son validas."
RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR = "Se ha presentado un error. No eres tu, somos nosotros!"
RESPONSE_MSG_GENERIC_ENV_ERROR = "Oh no! Lamentamos que no estemos para ti."