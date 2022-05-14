class Audit():

    def __init__(self):
        self.id = None
        self.service = None
        self.operation = None
        self.id_user = None
        self.response = None
        self.date = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_service(self):
        return self.service
 
    def set_service(self, service):
        self.service = service
    
    def get_operation(self):
        return self.operation
    
    def set_operation(self, operation):
        self.operation = operation
    
    def get_id_user(self):
        return self.idUser
    
    def set_id_user(self, id_user):
        self.id_user = id_user
    
    def get_response(self):
        return self.response
    
    def set_response(self, response):
        self.response = response
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date