"""
    @name - common
    @description - Funciones comunes del microservicio box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import HTTPException
import json


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
# EXCEPTION 
##########################################################

# @method - Genera una excepcion http
# @parameter - error - Json con el codigo y mensaje de error
# @return - HTTPException  
def get_http_exception(code:str, message:str) -> HTTPException:
    return HTTPException(status_code=code, detail=message)

def get_response_audit(data)-> str:
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
