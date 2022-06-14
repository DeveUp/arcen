import os
import request

from src.util.common import get_http_exception
from src.util.constant import FEIGN_ENDPOINT
from src.util.constant import RESPONSE_STATUS_CODE_GET, RESPONSE_STATUS_CODE_POST, RESPONSE_STATUS_CODE_PUT, RESPONSE_STATUS_CODE_DELETE
from src.util.constant import FEIGN_TYPE_GET, FEIGN_TYPE_POST, FEIGN_TYPE_PUT, FEIGN_TYPE_DELETE

class Feign:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        
    def request(self, endpoint, data):
        endpoint = self.endpoint + endpoint
        return os.environ.get(FEIGN_ENDPOINT) or endpoint
    
    def response(self, response, code_success= RESPONSE_STATUS_CODE_GET, code_error = None, message_error = None):
        print(response.status_code)
        isResponse = True if response.status_code == code_success else False
        if isResponse == False:
          raise get_http_exception(code_error, message_error)
        return isResponse

    def send(self, type:int, endpoint, data, code_error = None, message_error = None):
        endpoint = self.request(endpoint, data)
        response = None
        code_success = RESPONSE_STATUS_CODE_GET
        if type == FEIGN_TYPE_GET:
            code_success = RESPONSE_STATUS_CODE_GET
            response = requests.get(endpoint, json= data)
        if type == FEIGN_TYPE_POST:
            code_success = RESPONSE_STATUS_CODE_POST
            response = requests.post(endpoint, json= data)        
        if type == FEIGN_TYPE_PUT:
            code_success = RESPONSE_STATUS_CODE_PUT
            response = requests.put(endpoint, json= data)
        if type == FEIGN_TYPE_DELETE:
            code_success = RESPONSE_STATUS_CODE_DELETE
            response = requests.delete(endpoint, json= data)
        self.response(response, code_success, code_error, message_error)
        return response    

    def get(self, endpoint, data, code_error = None, message_error = None):
        return self.send(FEIGN_TYPE_GET, endpoint, data, code_error, message_error)    

    def post(self, endpoint, data, code_error = None, message_error = None):
       return self.send(FEIGN_TYPE_POST, endpoint, data, code_error, message_error)    
    
    def put(self, endpoint, data, code_error = None, message_error = None):
        return self.send(FEIGN_TYPE_PUT, endpoint, data, code_error, message_error)    
    
    def delete(self, endpoint, data, code_error = None, message_error = None):
        return self.send(FEIGN_TYPE_DELETE, endpoint, data, code_error, message_error)   