"""
    @description - Feign - Comunicacion con otros servicios o microservicios.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from src.util.constant import FEIGN
from src.util.constant import RESPONSE_GENERIC
from src.util.common import get_exception_http 

class Feign:

    # @method - Contructor 
    # @return - Void
    def __init__(self, endpoint):
        self.endpoint = endpoint
        # Se conoce las respuestas esperada por cada metodo
        self.operation_get = FEIGN['operation'][0]
        self.operation_post = FEIGN['operation'][1]
        self.operation_put = FEIGN['operation'][2]
        self.operation_delete = FEIGN['operation'][3]
    
    # @method - Valida la peticion del servicio
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Informacion a validar
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - String
    def request(self, endpoint, data, error):
        if data == None or endpoint == None:
            raise get_exception_http(error)
        endpoint = self.endpoint + endpoint
        return endpoint
    
    # @method - Valida la respuesta del servicio
    # @parameter - response - Json con la respuesta del servicio
    # @parameter - code_success - Codigo exitoso
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Boolean
    def is_response(self, response, code_success, error):
        if response == None:
            is_response = False
        else:
            try:
                is_response = True if response.status_code == code_success else False
            except:
                is_response = False
        if is_response == False:
            raise get_exception_http(error)
        return is_response

    # @method - Envia la peticion al servicio
    # @parameter - type - El metodo http a utilizar
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Json de la peticion del servicio
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Json
    def send(self, type:int, endpoint, data, error):  
        # Se valida el punto de entrada y la informacion
        endpoint = self.request(endpoint, data, error)
        response = None
        # Se consulta el metodo a utilizar la peticion
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        try:
            if type == self.operation_post:
                # Peticion por el metodo POST
                code_success = FEIGN['response']['success']['post']['code']
                response = session.post(endpoint, json= data, verify= False)        
            elif type == self.operation_put:
                # Peticion por el metodo PUT
                code_success = FEIGN['response']['success']['put']['code']
                response = session.put(endpoint, json= data, verify= False)
            elif type == self.operation_delete:
                # Peticion por el metodo DELETE
                code_success = FEIGN['response']['success']['delete']['code']
                response = session.delete(endpoint, json= data, verify=False)
            else:
                # Peticion por el metodo GET
                code_success = FEIGN['response']['success']['get']['code']
                response = session.get(endpoint, json= data, verify= False)
        except requests.exceptions.ConnectionError:
            raise get_exception_http(RESPONSE_GENERIC['system']['feign']['error']['connection'])
        except requests.Timeout:
            raise get_exception_http(RESPONSE_GENERIC['system']['feign']['error']['timeout'])
        except:
            raise get_exception_http(RESPONSE_GENERIC['system']['feign']['error']['default'])      
        # Se valida la respuesta del servicio
        self.is_response(response, code_success, error)
        return response    

    # @method - Envia la peticion al servicio con el metodo get
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Json de la peticion del servicio
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Json
    def get(self, endpoint, data, error = None):
        return self.send(self.operation_get, endpoint, data, error)    

    # @method - Envia la peticion al servicio con el metodo post
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Json de la peticion del servicio
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Json
    def post(self, endpoint, data, error = None):
       return self.send(self.operation_post, endpoint, data, error)    
    
    # @method - Envia la peticion al servicio con el metodo put
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Json de la peticion del servicio
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Json
    def put(self, endpoint, data, error = None):
        return self.send(self.operation_put, endpoint, data, error)    
    
    # @method - Envia la peticion al servicio con el metodo delete
    # @parameter - endpoint - Punto de entrada del servicio
    # @parameter - data - Json de la peticion del servicio
    # @parameter - error - Json con el codigo y mensaje de error
    # @return - Json
    def delete(self, endpoint, data, error = None):
        return self.send(self.operation_delete, endpoint, data, error)    