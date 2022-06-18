"""
    @description - Feign - Comunicacion con otros servicios o microservicios.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
import os
import requests

from src.util.constant import FEIGN
from src.util.common import get_exception_http

class Feign:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        # Se conoce las respuestas esperada por cada metodo
        self.operation_get = FEIGN['operation'][0]
        self.operation_post = FEIGN['operation'][1]
        self.operation_put = FEIGN['operation'][2]
        self.operation_delete = FEIGN['operation'][3]
        
    def request(self, endpoint, data):
        endpoint = self.endpoint + endpoint
        return os.environ.get(FEIGN_ENDPOINT) or endpoint
    
    def response(self, response, code_success, error):
        try:
            isResponse = True if response.status_code == code_success else False
        except:
            isResponse = False
        finally:
            if isResponse == False:
                raise get_exception_http(error)
        return isResponse

    def send(self, type:int, endpoint, data, error):  
        # Se valida el punto de entrada y la informacion
        endpoint = self.request(endpoint, data)
        response = None
        # Se consulta el metodo a utilizar la peticion
        code_success = FEIGN['response']['success']['get']['code']
        if type == self.operation_get:
            # Peticion por el metodo GET
            code_success = FEIGN['response']['success']['get']['code']
            response = requests.get(endpoint, json= data)
        elif type == self.operation_post:
            # Peticion por el metodo POST
            code_success = FEIGN['response']['success']['post']['code']
            response = requests.post(endpoint, json= data)        
        elif type == self.operation_put:
            # Peticion por el metodo PUT
            code_success = FEIGN['response']['success']['put']['code']
            response = requests.put(endpoint, json= data)
        elif type == self.operation_delete:
            # Peticion por el metodo DELETE
            code_success = FEIGN['response']['success']['delete']['code']
            response = requests.delete(endpoint, json= data)
        # Se valida la respuesta
        self.response(response, code_success, error)
        return response    

    def get(self, endpoint, data, error = None):
        return self.send(self.operation_get, endpoint, data, error)    

    def post(self, endpoint, data, error = None):
       return self.send(self.operation_post, endpoint, data, error)    
    
    def put(self, endpoint, data, error = None):
        return self.send(self.operation_put, endpoint, data, error)    
    
    def delete(self, endpoint, data, error = None):
        return self.send(self.operation_delete, endpoint, data, error)    