from fastapi import HTTPException

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