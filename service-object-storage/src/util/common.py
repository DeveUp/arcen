def get_validate_field(data:str, key:str):
    try:
        field= data[key]
    except:
        field = None
    return field