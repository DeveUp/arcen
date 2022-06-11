from fastapi import HTTPException
from datetime import datetime
import json

from src.util.constant import FORMAT_DATE

def is_generic_date(str_date:str, format:str): 
    try:
        datetime.strptime(str_date, format)
    except ValueError:
        return False
    return True

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

def generate_date(format:str=FORMAT_DATE):
    return str(datetime.today().strftime(format))
    