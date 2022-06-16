import bson
import uuid
import os
import socket

from datetime import datetime
from fastapi import HTTPException

from src.util.constant import UTIL
from src.util.constant import RESPONSE_GENERIC

##########################################################
# IS
##########################################################

# @Method - Verifica si una cadena es una fecha valida
# @Parameter - str_date - Representa la cadena a validar
# @Parameter - format - Formato de la fecha
# @Return - Boolean
def is_generic_date(str_date:str, format:str): 
    try:
        datetime.strptime(str_date, format)
    except ValueError:
        return False
    return True

# @Method - Verifica si una cadena es una fecha valida
# @Parameter - str_date - Representa la cadena a validar
# @Parameter - format (Optional) - Formato a validar AAAA-MM-DD
# @Return - Boolean
def is_date(str_date:str, format:str=UTIL['format']['date'][0]): 
    return is_generic_date(str_date, format)

# @Method - Verifica si una cadena es una fecha valida
# @Parameter - str_date - Representa la cadena a validar
# @Parameter - format (Optional) - Formato a validar AAAA-MM-DD HH-MM
# @Return - Boolean
def is_date_time(str_date:str, strict:bool=False, format:str=UTIL['format']['date'][1]): 
    rta = is_generic_date(str_date, format)
    if rta == False and strict == False:
        rta = is_date(str_date)
    return rta

##########################################################
# GENERATE
##########################################################

# @Method - Genera una cadena con la fecha actual
# @Parameter - format (Optional) - Formato a de la fecha AAAA-MM-DD HH-MM
# @Return - String
def generate_date(format:str=UTIL['format']['date'][1]):
    return str(datetime.today().strftime(format))

# @Method - Genera la direccion de ip actual
# @Return - String
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# @Method - Genera un id unico
# @Return - String
def generate_id(type:int=1):
    id = None
    if type == 1:
        id = str(bson.ObjectId())
    if type == 2:
        id = str(uuid.uuid1())
    if id == None:
        return generate_id(type)
    return id

##########################################################
# VALIDATOR
##########################################################

# @Method - Valida que un objecto tenga una clave
# @Parameter - data - Representa el objeto
# @Parameter - key - Representa la clave
# @Parameter - default - Representa el valor por defecto si no existe la clave
# @Return - String
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
# REPLACE
##########################################################

# @Method - Elimina caracteres especiales de una cadena (Fecha)
# @Parameter - str_date - Representa la fecha en cadena
# @Return - String
def replace_character_date(str_date:str): 
    str_date = str_date.replace("%20", ' ')
    str_date = str_date.replace("%3A", ':')
    str_date = str_date.replace("pm", '')
    str_date = str_date.replace("am", '')
    return str_date

##########################################################
# EXCEPTION 
##########################################################

# @Method - Genera una excepcion http
# @Parameter - error - Json con el codigo y mensaje de error
# @Return - HTTPException
def get_exception_http(error) -> HTTPException:
    return get_exception_http_build(error['code'], error['msg'])

# @Method - Genera una excepcion http
# @Parameter - code - Representa el codigo error
# @Parameter - message - Representa el mensaje de error
# @Return - HTTPException
def get_exception_http_build(code:str, message:str) -> HTTPException:
    return HTTPException(status_code=code, detail=message)

##########################################################
# FIND 
##########################################################

# @Method - Busca el valor de una variable de entorno por su nombre
# @Parameter - name - Representa el nombre
# @Return - Object
def find_env(name:str):
    try:
        value = os.environ[name]
        print(value)
    except:
        get_exception_http(RESPONSE_GENERIC['system']['env']['error']['default'])
    return value