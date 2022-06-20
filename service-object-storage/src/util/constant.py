"""
    @name - constant
    @description - Constantes para el microservicio objecto
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

# @json - Puntos de entradas a los servicios (Objecto)
# @content - path - Entrada principal
# @content - service.object - Entrada objecto
# @content - service.subobject - Entrada subobjecto
# @content - service.type_object - Entrada tipo objecto
ENDPOINT = {
    "path": "/api",
    "service": {
        "object": {
           "path": "/object",
        },
        "subobject": {
            "path": "/subobject"
        },
        "type_object": {
           "path": "/type-object" 
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
        },
        "put":{
            "update": "/{id}"
        },
        "delete":{
            "delete_by_id": "/{id}"
        }
    }
}

# @json - Base de datos del microservicio objecto
# @content - table.object - Tabla objecto
# @content - table.subobject - Tabla subobjecto
# @content - table.type_object - Tabla tipo objecto
DATABASE= {
    "table":{
        "object":{
            "name": "object",
            "pk": "id",
            "column": [
                "id",
                "id_type_object",
                "id_sub_object",
                "date"
            ]
        },
        "subobject":{
            "name": "object-subobject",
            "pk": "id",
            "column": [
                "id",
                "number",
                "box",
                "date"
            ]
        },
        "type_object":{
            "name": "type-object",
            "pk": "id",
            "column": [
                "id",
                "name",
                "height",
                "width",
                "depth",
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
            "object":  "OBJECT",
            "type_object": "TYPE_OBJECT",
            "subobject": "SUBOBJECT"
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

# @json - Respuestas servicios del microservicio de objecto
# @Content - object - Respuesta objecto
RESPONSE = {
    "object":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del objecto")
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
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el objecto")
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
                        "msg":  RESPONSE_GENERIC['put']['update']['error']['default']['msg']%("el objecto")
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
                        "msg":  RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['msg']%("el objecto")
                    }
                }
            }
        }   
    },
    "type_object":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del tipo de objecto")
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
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el tipo de objecto")
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
                        "msg":  RESPONSE_GENERIC['put']['update']['error']['default']['msg']%("el tipo de objecto")
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
                        "msg":  RESPONSE_GENERIC['delete']['delete_by_id']['error']['default']['msg']%("el tipo de objecto")
                    }
                }
            }
        }   
    }
}




# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_OBJECT = "/object"
ENDPOINT_APP_SUB_OBJECT = "/sub-object"
ENDPOINT_APP_TYPE_OBJECT = "/type-object"

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
DATABASE_POSTGRESQL_DATABASE = "arcen_object";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://arcen:arcen@arcen-postgresql:5432/arcen"

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_OBJECT = "object"
DATABASE_POSTGRESQL_TABLE_SUB_OBJECT= "sub_object"
DATABASE_POSTGRESQL_TABLE_TYPE_OBJECT = "type_object"

# COLUMNA OBJECT
COLUMN_OBJECT = "object"
COLUMN_OBJECT_ID = "id"
COLUMN_OBJECT_ID_TYPE_OBJECT = "id_type_object"
COLUMN_OBJECT_ID_SUB_OBJECT = "id_sub_object"
COLUMN_OBJECT_CREATION_DATE = "date"

# COLUMNA SUB_OBJECT
COLUMN_SUB_OBJECT = "sub_object"
COLUMN_SUB_OBJECT_ID = "id"
COLUMN_SUB_OBJECT_NUMBER = "number"
COLUMN_SUB_OBJECT_BOX = "box"
COLUMN_SUB_OBJECT_CREATION_DATE = "date"

# COLUMNA TYPE_OBJECT
COLUMN_TYPE_OBJECT = "type_object"
COLUMN_TYPE_OBJECT_ID = "id"
COLUMN_TYPE_OBJECT_NAME = "name"
COLUMN_TYPE_OBJECT_HEIGHT = "height"
COLUMN_TYPE_OBJECT_WIDTH = "width"
COLUMN_TYPE_OBJECT_DEPTH = "depth"
COLUMN_TYPE_OBJECT_CREATION_DATE = "date"
