"""
    @name - constant
    @description - Constantes para el microservicio objeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""

# @JSON - Utilidades
# @Content - format - Representa formatos a utilizar
UTIL = {
    "format":{
        "response": [
            "code",
            "msg",
            "operation"
        ]
    }
}

# @json - Base de datos del microservicio mueble
# @content - table.block - Tabla bloque
# @content - table.furniture - Tabla mueble
# @content - table.type_furniture - Tabla tipo mueble
DATABASE= {
    "table":{
        "block":{
            "name": "block",
            "pk": "id",
            "column": [
                "id",
                "letter",
                "flat",
                "date"
            ]
        },
        "furniture":{
            "name": "furniture",
            "pk": "id",
            "column": [
                "id",
                "id_block",
                "id_type_furniture",
                "number_furniture",
                "date"
            ]
        },
        "type_furniture":{
            "name": "type-furniture",
            "pk": "id",
            "column": [
                "id",
                "number_type_furniture",
                "count_rack",
                "count_row",
                "depth",
                "height",
                "width",
                "date"
            ]
        }
    }
} 

# @json - Codigos repsuesta generico
# @content - success - Codigos exitosos
# @content - error - Codigos de error
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

# @json - Repsuestas genericas
# @content - get 
# @content - post
# @content - system
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
                },
                "exist": {
                    "code": RESPONSE_GENERIC_CODE['error']['request'],
                    "msg": "¡Ups! verifique el nombre %s, encontramos almenos un resultado."
                }
            }
        },
        "find_all":{
            "response": list,
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['find']
                } 
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['find'],
                    "msg": "¡Och! no encontramos ningun%s resultado."
                }
            }
        },
        "find_by_range_date_all": {
            "response": list,
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
                    "msg": "Ouch! No pudimos registrar %s. Vuelva a intentar mas tarde!"
                }
            }
        }
    },
    "put":{
        "update": {
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['update']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['update'],
                    "msg": "Ouch! No pudimos actualizar %s. Vuelva a intentar mas tarde!"
                }
            }
        }
    },
    "delete":{
        "delete_by_id": {
            "success": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['success']['delete']
                }
            },
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['delete'],
                    "msg": "Ouch! No pudimos eliminar %s. Vuelva a intentar mas tarde!"
                },
                "dependence": {
                    "code": RESPONSE_GENERIC_CODE['error']['delete'],
                    "msg": "Ouch! No pudimos eliminar %s. Tiene dependencia %s."
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
        },
        "feign":{
            "error": {
                "default": {
                    "code": RESPONSE_GENERIC_CODE['error']['request'],
                    "msg": "Oh no! No eres tu somos nosotros hemos tenido un problema."
                },
                "connection": {
                    "code": RESPONSE_GENERIC_CODE['error']['request'],
                    "msg": "Oh no! Nuestra conexion esta inestable, esperamos estar pronto para ti."
                },
                "timeout":{
                    "code": RESPONSE_GENERIC_CODE['error']['request'],
                    "msg": "Oh no! Se ha agotado el tiempo."
                }
            }
        }
    }
}

# @json - Comunicacion con otros microservicios
# @content - service.operation - Operaciones expone feign
FEIGN = {
    "operation":[
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "response":{
        "success":{
            "get":{
                "code": RESPONSE_GENERIC_CODE['success']['find']
            },
            "post":{
                "code": RESPONSE_GENERIC_CODE['success']['save']
            },
            "put":{
                "code": RESPONSE_GENERIC_CODE['success']['update']
            },
            "delete":{
                "code": RESPONSE_GENERIC_CODE['success']['delete']
            }
        }
    },
    "type":{
        "generic": {
            "get": {
                "find_by_id": "FIND_BY_ID"
            },
            "post":{
                "save": "SAVE",
            },
            "put": {
                "update": "UPDATE"
            },
            "delete":{
                "delete_by_id": "DELETE_BY_ID"
            }
        },
        "service": {
            "block":  "BLOCK",
            "furniture": "FURNITURE",
            "type_furniture": "TYPE_FURNITURE"
        }
    },
    "microservice": {
        "audit": {
            "service": {
                "audit": {
                    "response":{
                        "error":{
                            "default": {
                                "code": RESPONSE_GENERIC_CODE['error']['save'],
                                "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("la auditoria")
                            } 
                        }
                    }
                }
            }  
        }
    }
}

# @json - Respuestas servicios del microservicio de mueble
# @Content - block - Respuesta bloque
RESPONSE = {
    "block":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del bloque")
                    }
                }
            },
            "find_all": RESPONSE_GENERIC['get']['find_all']
        },  
        "post":{
            "save":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el bloque")
                    }
                }
            }
        },
        "put":{
            "update":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['put']['update']['error']['default']['msg']%("el bloque")
                    }
                }
            }
        },
        "delete":{
            "delete_by_id":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['msg']%("el bloque")
                    }
                }
            }
        }   
    },
    "furniture":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del mueble")
                    }
                }
            },
            "find_all": RESPONSE_GENERIC['get']['find_all']
        },  
        "post":{
            "save":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el mueble")
                    }
                }
            }
        },
        "put":{
            "update":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['put']['update']['error']['default']['msg']%("el mueble")
                    }
                }
            }
        },
        "delete":{
            "delete_by_id":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['msg']%("el mueble")
                    }
                }
            }
        }   
    },
    "type_furniture":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del tipo de mueble")
                    }
                }
            },
            "find_all": RESPONSE_GENERIC['get']['find_all']
        },  
        "post":{
            "save":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el tipo de mueble")
                    }
                }
            }
        },
        "put":{
            "update":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['put']['update']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['put']['update']['error']['default']['msg']%("el tipo de mueble")
                    }
                }
            }
        },
        "delete":{
            "delete_by_id":{
                 "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['msg']%("el tipo de mueble")
                    }
                }
            }
        }   
    }
}




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
DATABASE_POSTGRESQL_URL = "postgresql://arcen:arcen@arcen-postgresql:5432/arcen"

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
FEIGN_ENDPOINT_AUDIT = "http://127.0.0.3:8001/api/audit"
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