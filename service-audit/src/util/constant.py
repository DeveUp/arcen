# @JSON - Utilidades
# @Content - format - Representa formatos
UTIL = {
    "format":{
        "date": [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M'
        ]
    }
}

# @JSON - Puntos de entradas a los servicios
# @Content - path - Entrada principal
# @Content - service.audit - Entrada auditoria
# @Content - service.audit_closure - Entrada cierre de auditoria
# @Content - service.control_audit - Entrada control de auditoria
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
                    "find_by_id": "/{id}/table-id/{table}",
                    "find_all": "/table-id/{table}"
                }
            }
        },
        "control_audit": {
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

# @JSON - Base de datos
# @Content - table.audit - Tabla auditoria
# @Content - table.audit_closure - Tabla cierre de auditoria
# @Content - table.control_audit - Tabla control de auditoria
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
                ["date_start", "date_end"]
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
            "subname": "audit-closure",
            "pk": "_id",
            "column": [
                "id",
                "control",
                "audit",
                "date",
                ["date_start", "date_end"]
            ]
        }
    }
}


# @JSON - Codigo repsuesta generico
# @Content - success - Codigos exitosos
# @Content - error - Codigos de error
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

# @JSON - Repsuesta generico
# @Content - get 
# @Content - post 
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

# @JSON - Repsuesta servicios
# @Content - audit - Resppuestas Auditoria
# @Content - control_audit - Resppuestas  control de auditoria
# @Content - audit_closure - Resppuestas  cierre de auditoria
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
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_all']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['get']['find_all']['error']['default']['msg']%("")
                    }
                }
            },
            "find_by_range_date_all": RESPONSE_GENERIC['get']['find_by_range_date_all']
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
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("la auditoria")
                    }
                }
            }
        }    
    },
    "control_audit":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del control de auditoria")
                    }
                }
            },
            "find_by_name":{
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_name']['success']['default']['code']
                    }
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['get']['find_by_name']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['get']['find_by_name']['error']['default']['msg']%("del control de auditoria")
                    },
                    "exist": {
                        "code": RESPONSE_GENERIC['get']['find_by_name']['error']['exist']['code'],
                        "msg":  RESPONSE_GENERIC['get']['find_by_name']['error']['exist']['msg']%("del control de auditoria")
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
                },
                "error": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['error']['default']['code'],
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el control de auditoria")
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
                "response": list,
                "success": {
                    "default": {
                        "code": RESPONSE_GENERIC['post']['save']['success']['default']['code']
                    }
                },
                "error":{
                    "range_date": RESPONSE_GENERIC['get']['find_by_range_date_all']['error']['default']
                }
            }
        }  
    }
}