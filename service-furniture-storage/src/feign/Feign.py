import os
import requests

from src.util.common import get_http_exception

class Feign:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        
    def validate_request(self, endpoint, data):
        endpoint = self.endpoint + endpoint
        return os.environ.get('endpoint') or endpoint
    
    def validate_response(self, response, code_error = None, message_error = None):
        isResponse = True if response.status_code == 200 else False
        if isResponse == False:
          raise get_http_exception(code_error, message_error)
        return isResponse

    def get(self, endpoint, data, code_error = None, message_error = None):
        endpoint = self.validate_request(endpoint, data)
        response = requests.get('{endpoint}', data= data)
        self.validate_response(response, code_error, message_error)
        return response    

    def post(self, endpoint, data, code_error = None, message_error = None):
        endpoint = self.validate_request(endpoint, data)
        response = requests.post(endpoint, data= data)
        self.validate_response(response, code_error, message_error)
        return response
    
    def put(self, endpoint, data, code_error = None, message_error = None):
        endpoint = self.validate_request(endpoint, data)
        response = requests.put('{endpoint}', data= data)
        self.validate_response(response, code_error, message_error)
        return response
    
    def delete(self, endpoint, data, code_error = None, message_error = None):
        endpoint = self.validate_request(endpoint, data)
        response = requests.delete('{endpoint}', data= data)
        self.validate_response(response, code_error, message_error)
        return response