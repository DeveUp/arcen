"""
    @description - Constantes para el microservicio digitalizacion
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""

# @JSON - Utilidades
# @Content - format - Representa formatos a utilizar
UTIL = {
    "format":{
        "date": [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M'
        ]
    }
}

# @json - Puntos de entradas a los servicios (Digitalizacion)
# @content - path - Entrada principal
# @content - service.document - Entrada documento
# @content - service.document_location - Entrada ubicacion documento
# @content - service.document_version - Entrada version documento
# @content - service.invoice - Entrada folio
# @content - service.invoice_status - Entrada estado folio
ENDPOINT = {
    "path": "/api",
    "service": {
        "document": {
           "path": "/document",
        },
        "document_location": {
            "path": "/document-location"
        },
        "document_version": {
           "path": "/document-version" 
        },
        "invoice": {
           "path": "/invoice" 
        },
        "invoice_status": {
           "path": "/invoice-status" 
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

# @json - Base de datos del microservicio digitalizacion
# @content - table.document - Tabla documento
# @content - table.document_location - Tabla ubicacion documento
# @content - table.document_version - Tabla version documento
# @content - table.invoice - Tabla folio
# @content - table.invoice_status - Tabla estado folio
DATABASE= {
    "table":{
        "document":{
            "name": "document",
            "pk": "_id",
            "column": [
                "id",
                "id_document_location",
                "name",
                "document",
                "path_document",
                "date"
            ]
        },
        "document_location":{
            "name": "document-location",
            "pk": "_id",
            "column": [
                "id",
                "name",
                "id_object",
                "id_invoice",
                "date"
            ]
        },
        "document_version":{
            "name": "document-version",
            "pk": "_id",
            "column": [
                "id",
                "id_document_location",
                "version",
                "date"
            ]
        },
        "invoice":{
            "name": "invoice",
            "pk": "_id",
            "column": [
                "id",
                "name",
                "index_number",
                "id_invoice_statu",
                "security_level",
                "date"
            ]
        },
        "invoice_status":{
            "name": "invoice-status",
            "pk": "_id",
            "column": [
                "id",
                "name",
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
    }
}

# @json - Repsuestas genericas
# @content - get 
# @content - post 
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


# @json - Respuestas servicios del microservicio de digitalizacion
# @Content - documento - Respuesta documento
RESPONSE = {
    "document":{
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
                        "msg":  RESPONSE_GENERIC['get']['find_by_id']['error']['default']['msg']%("del documento")
                    }
                }
            },
            "find_all": RESPONSE_GENERIC['get']['find_all'],
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
                        "msg":  RESPONSE_GENERIC['post']['save']['error']['default']['msg']%("el documento")
                    }
                }
            }
        }    
    }
}