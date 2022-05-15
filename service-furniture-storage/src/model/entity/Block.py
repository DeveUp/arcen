class Block():

    def __init__(self):
        self.id = None
        self.letter = None
        self.flat = None
        self.date = None
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def get_flat(self):
        return self.flat

    def set_flat(self, flat):
        self.flat = flat
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date