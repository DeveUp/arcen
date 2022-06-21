"""
    @name - common
    @description - Funciones comunes del microservicio mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
import os
import json

from fastapi import HTTPException

from src.util.constant import RESPONSE_GENERIC

##########################################################
# VALIDATOR
##########################################################

# @method - Valida que un objeto tenga una clave
# @parameter - data - Representa el objeto
# @parameter - key - Representa la clave
# @parameter - default - Representa el valor por defecto si no existe la clave
# @return - String
def get_validate_field(data:str, key:str, default = None):
    try:
        field= data[key]
    except ValueError:
        field = default
    except AttributeError:
        field = default
    except:
        field = default
    return field

##########################################################
# CONVERT
##########################################################

# @method - Convierte un string a string buffer
# @parameter - data - Representa el string
# @return - String Buffer
def convert_json(data)-> str:
    if data == None:
        return "None"
    element = data
    if type(data) != 'dict':
        element = dict(data)
    try:
        data = json.dumps(element)
    except:
        data = str(element)
    finally:
        if data == None:
            data = "None"
    return data

##########################################################
# EXCEPTION 
##########################################################

# @method - Genera una excepcion http
# @parameter - error - Json con el codigo y mensaje de error
# @return - HTTPException
def get_exception_http(error) -> HTTPException:
    return get_exception_http_build(error['code'], error['msg'])

# @method - Genera una excepcion http
# @parameter - code - Representa el codigo error
# @parameter - message - Representa el mensaje de error
# @return - HTTPException
def get_exception_http_build(code:str, message:str) -> HTTPException:
    return HTTPException(status_code=code, detail=message)

##########################################################
# FIND 
##########################################################

# @method - Busca el valor de una variable de entorno por su nombre
# @parameter - name - Representa el nombre
# @return - Object
def find_env(name:str):
    try:
        value = os.environ[name]
    except:
        get_exception_http(RESPONSE_GENERIC['system']['env']['error']['default'])
    return value