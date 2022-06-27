"""
    @description - Funciones especificas para el microservicio digitalizacion
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
import base64
from PIL import Image
import io 
import os
import img2pdf

from src.util.common import find_env
from src.util.common import generate_id

def encode(data:str, folder:str, file_name:str, ext:str='jpeg', separator:str= '.'):
    image = base64.b64decode(data)  
    img = Image.open(io.BytesIO(image))
    imagePath = folder + file_name + separator + ext
    img.save(imagePath, ext)
    return [imagePath, ext]

def create_path_image(separator_end:bool= True, pk:bool= True, type_pk:int= 1):
    separator = str(find_env("APP_PATH_TMP_IMAGE_SEPARATOR"))
    path_image = str(find_env("APP_PATH_TMP_IMAGE"))
    path = list()
    if separator_end == True or pk == True:
        path.append(path_image)
        path.append(separator)
    else:
        path.append(path_image)
    if pk == True:
        path.append(str(generate_id(type_pk)) )
        path.append(separator)
    path_image = "".join(path)
    return path_image

def create_folder(folder:str):
    is_dir = os.path.isdir(folder)
    if is_dir == False:
        try:
            os.mkdir(folder)
        except OSError as e:
            print(e)
            return False
    return True

def convert_images_to_pdf(folder:str, filename:str, ext:str = '.jpeg', ext_pdf= '.pdf'):
    print("Se va consultar las imagenes......")
    imagenes = [archivo for archivo in os.listdir(folder) if archivo.endswith(ext)]
    print("Images...........")
    print(imagenes)
    path_pdf = str(find_env("APP_PATH_PDF")) + filename +ext_pdf
    print(path_pdf)
    with open(path_pdf, "wb") as documento:
	    documento.write(img2pdf.convert(imagenes))
    
