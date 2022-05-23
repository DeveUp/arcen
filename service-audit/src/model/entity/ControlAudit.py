class ControlAudit():

    def __init__(self):
        self.id = None
        self.name = None
        self.date_start = None
        self.date_end = None
        self.date = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
 
    def set_name(self, name):
        self.name = name
    
    def get_date_start(self):
        return self.date_start
    
    def set_date_start(self, date_start):
        self.date_start = date_start
    
    def get_date_end(self):
        return self.date_end
    
    def set_date_end(self, date_end):
        self.date_end = date_end
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date