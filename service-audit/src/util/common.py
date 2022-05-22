from datetime import datetime
from email.policy import strict

from src.util.constant import FORMAT_DATE_STR, FORMAT_DATE

def replaceCharacterDate(str_date:str): 
    str_date = str_date.replace("%20", ' ')
    str_date = str_date.replace("%3A", ':')
    str_date = str_date.replace("pm", '')
    str_date = str_date.replace("am", '')
    return str_date

def isDate(str_date:str): 
    return isGenericDate(str_date, FORMAT_DATE_STR)

def isDateTime(str_date:str, strict:bool = False): 
    rta = isGenericDate(str_date, FORMAT_DATE)
    if rta == False and strict == False:
        rta = isDate(str_date)
    return rta

def isGenericDate(str_date:str, format:str): 
    try:
        datetime.strptime(str_date, format)
    except ValueError:
        return False
    return True