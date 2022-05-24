class Audit():

    def __init__(self):
        self.id:str = None
        self.service:str = None
        self.operation:str = None
        self.id_user:str = None
        self.ip_address:str = None 
        self.response:str = None
        self.date:str = None

    def get_id(self) -> str:
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_service(self) -> str:
        return self.service
 
    def set_service(self, service):
        self.service = service
    
    def get_operation(self) -> str:
        return self.operation
    
    def set_operation(self, operation):
        self.operation = operation
    
    def get_id_user(self)-> str:
        return self.id_user
    
    def set_id_user(self, id_user):
        self.id_user = id_user
    
    def get_ip_address(self)-> str:
        return self.ip_address
    
    def set_ip_address(self, ip_address):
        self.ip_address = ip_address
    
    def get_response(self)-> str:
        return self.response
    
    def set_response(self, response):
        self.response = response
    
    def get_date(self)-> str:
        return self.date
    
    def set_date(self, date):
        self.date = date