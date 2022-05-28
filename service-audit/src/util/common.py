import bson
import uuid
import socket
from datetime import datetime
from fastapi import HTTPException

from src.util.constant import FORMAT_DATE_STR, FORMAT_DATE

def is_date(str_date:str): 
    return is_generic_date(str_date, FORMAT_DATE_STR)

def is_date_time(str_date:str, strict:bool = False): 
    rta = is_generic_date(str_date, FORMAT_DATE)
    if rta == False and strict == False:
        rta = is_date(str_date)
    return rta

def is_generic_date(str_date:str, format:str): 
    try:
        datetime.strptime(str_date, format)
    except ValueError:
        return False
    return True

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

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

def get_http_exception(code:str, message:str) -> HTTPException:
    return HTTPException(status_code=code, detail=message)


def replace_character_date(str_date:str): 
    str_date = str_date.replace("%20", ' ')
    str_date = str_date.replace("%3A", ':')
    str_date = str_date.replace("pm", '')
    str_date = str_date.replace("am", '')
    return str_date

def generate_id(type:int =1):
    id = None
    if type == 1:
        id = str(bson.ObjectId())
    if type == 2:
        id = str(uuid.uuid1())
    if id == None:
        return generate_id(type)
    return id

def generate_date(format:str=FORMAT_DATE):
    return str(datetime.today().strftime(format))