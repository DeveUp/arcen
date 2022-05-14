class Audit():
    def __init__(self, id, service, operation, id_user, response, date):
        self.id = id
        self.service = service
        self.operation = operation
        self.id_user = id_user
        self.response = response
        self.date = date

    @property
    def id(self):
        return self.id

    @id.setter 
    def id(self, id):
        self.id = id
    
    @property
    def service(self):
        return self.service

    @service.setter 
    def service(self, service):
        self.service = service
    
    @property
    def operation(self):
        return self.operation
    
    @operation.setter
    def operation(self, operation):
        self.operation = operation
    
    @property
    def id_user(self):
        return self.idUser
    
    @id_user.setter
    def id_user(self, id_user):
        self.id_user = id_user
    
    @property
    def response(self):
        return self.response
    
    @response.setter
    def response(self, response):
        self.response = response
    
    @property
    def date(self):
        return self.date
    
    @date.setter
    def date(self, date):
        self.date = date