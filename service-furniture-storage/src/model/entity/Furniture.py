class Furniture():

    def __init__(self):
        self.id = None
        self.id_block = None
        self.id_type_furniture = None
        self.number_furniture = None
        self.date = None
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_block(self):
        return self.id_block

    def set_id_block(self, id_block):
        self.id_block = id_block
    
    def get_id_type_furniture(self):
        return self.id_type_furniture

    def set_id_type_furniture(self, id_type_furniture):
        self.id_type_furniture = id_type_furniture

    def get_number_furniture(self):
        return self.number_furniture

    def set_number_furniture(self, number_furniture):
        self.number_furniture = number_furniture
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date